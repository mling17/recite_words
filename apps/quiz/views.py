from django import forms
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from apps.quiz.models import Quiz, QuizLog, QuizLogErr
from apps.word.models import Word, Lesson
import random
import datetime
import json


class BootStrapForm(object):
    bootstrap_class_exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrap_class_exclude:
                continue
            old_class = field.widget.attrs.get('class', "")
            field.widget.attrs['class'] = '{} form-control'.format(old_class)
            field.widget.attrs['placeholder'] = f'{field.label}'


class QuizCreateModelForm(BootStrapForm, forms.ModelForm):
    lessons = Lesson.objects.all()
    lesson_choice = []
    for lesson in lessons:
        name = f'{lesson.unit.book.name}||{lesson.unit.name}||{lesson.name}'
        lesson_choice.append((lesson.id, name))
    lesson = forms.MultipleChoiceField(choices=lesson_choice)

    class Meta:
        model = Quiz
        fields = ['description', 'lesson', 'amount', 'max_total_time', 'max_word_time']


def quiz(request):
    query_set = Quiz.objects.filter(author=request.user_info.user.id)
    # todo 添加课本和单元的显示
    return render(request, 'quiz_list.html', {'quiz_list': query_set})


def quiz_create(request):
    if request.method == 'GET':
        form = QuizCreateModelForm()
        return render(request, 'quiz_create.html', {'form': form})
    user = request.user_info.user
    form = QuizCreateModelForm(data=request.POST)
    if form.is_valid():
        description = form.cleaned_data.get('description')
        lesson = form.cleaned_data.get('lesson')
        amount = form.cleaned_data.get('amount')
        max_total_time = form.cleaned_data.get('max_total_time')
        max_word_time = form.cleaned_data.get('max_word_time')
        lesson = ','.join(lesson)
        new_quiz = Quiz()
        new_quiz.description = description
        new_quiz.author = user
        new_quiz.lesson = lesson
        new_quiz.amount = amount
        new_quiz.max_total_time = max_total_time
        new_quiz.max_word_time = max_word_time
        new_quiz.save()
        return redirect('quiz:quiz_list')
    else:
        return render(request, 'quiz_create.html', {'form': form})


def quiz_start(request, q_id):
    query_set = Quiz.objects.filter(id=int(q_id)).first()
    amount = query_set.amount
    return render(request, 'quiz_start.html', {'q_id': q_id, 'amount': amount})


def quiz_result(request, q_id):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        QuizLog.user = request.user_info.user
        QuizLog.quiz_id = q_id
        QuizLog.start_time = data['start_time']
        QuizLog.finish_time = datetime.datetime.now()
        QuizLog.amount = data.get('amount')
        QuizLog.correct_count = data.get('correct_count')
        error_words = data.get('error_words')
        correct_words = data.get('correct_words')
        qle_list = []
        for err_word in error_words:
            qle = QuizLogErr(quiz_id=q_id, word_id=err_word[0], wrong=err_word[1])
            qle_list.append(qle)
        QuizLogErr.objects.bulk_create(qle_list)

    return HttpResponse('over')


def get_quiz_question(request):
    q_id = request.GET.get('q_id')
    quiz_info = Quiz.objects.filter(id=int(q_id)).first()
    lesson = quiz_info.lesson.split(',')
    lesson = list(map(lambda x: int(x), lesson))
    res = Word.objects.filter(lesson_id__in=lesson).values_list('id', 'word', 'symbol', 'cn', 'word_type')
    word_list = list(res)
    random.shuffle(word_list)
    amount = quiz_info.amount
    if amount != 0:
        amount = amount if len(word_list) > amount else len(word_list)
        word_list = word_list[:amount]
    else:
        word_list = word_list[:]
        amount = len(word_list)

    data = {
        'id': q_id,  # quiz_id
        'desc': quiz_info.description,  # 描述
        'amount': amount,  # 题目数量
        'start_time': datetime.datetime.now(),  # 开始时间
        'max_total_time': 7200,  # 答题时间
        'word_list': word_list
    }
    return JsonResponse(data)
