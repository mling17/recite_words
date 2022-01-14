from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe
from django.db.models import Count
from apps.word import models
from utils.pagination import Pagination
import json


# Create your views here.
def book_data(query_set):
    data = list(query_set)
    res = {}
    for item in data:
        book_name = item['book_name']
        unit = item['unit']
        res.update({book_name: {'name': book_name, 'unit': {}}})
    for item in data:
        book_name = item['book_name']
        unit = item['unit']
        res[book_name]['unit'].update({unit: []})
    for item in data:
        book_name = item['book_name']
        unit = item['unit']
        classes = item['classes']
        res[book_name]['unit'][unit].append(classes)
    return res


def word_list(request):
    if request.method == 'GET':
        book = request.GET.get('book_name', -1)
        unit = request.GET.get('unit', -1)
        lesson = request.GET.get('lesson', -1)
        if str(book) == '-1' or book is None:
            queryset = models.Words.objects.all()
        else:
            if str(unit) == '-1':
                queryset = models.Words.objects.filter(book_name=book)
            else:
                if str(lesson) == '-1':
                    queryset = models.Words.objects.filter(book_name=book, unit=int(unit))
                else:
                    queryset = models.Words.objects.filter(book_name=book, unit=int(unit), classes=int(lesson))
        page_object = Pagination(
            current_page=request.GET.get('page'),
            all_count=queryset.count(),
            base_url=request.path_info,
            query_params=request.GET
        )
        words_obj_list = queryset[page_object.start:page_object.end]
        # ### 搜索
        word_group = models.Words.objects.values('book_name', 'unit', 'classes').annotate(counts=Count('book_name'))
        word_group = book_data(word_group)
        # ### 搜索 end
        context = {
            'word_object_list': words_obj_list,
            'page_html': page_object.page_html(),
            'word_group': word_group,
            'query_params': {'book_name': book, 'unit': unit, 'lesson': lesson}
        }
        return render(request, 'words.html', context)


from apps.stark.service.v1 import StarkHandler
from apps.stark.service.v1 import Option


class WordHandler(StarkHandler):
    list_display = ['unit', 'classes', 'word', 'symbol', 'cn']
    # search_group = [Option('unit'), Option('classes')]
    search_list = ['word', 'symbol', 'cn']


def word_test(request):
    return render(request, 'learn_records.html')
