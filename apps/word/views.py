from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe
from django.db.models import Count
from apps.word import models
from utils.pagination import Pagination


# Create your views here.
def book_data(query_set):
    data = list(query_set)
    res = {}
    for item in data:
        book_name = item['book_name']
        unit = item['unit']
        res.update({book_name: {'name': book_name}})
    for item in data:
        book_name = item['book_name']
        unit = item['unit']
        res[book_name].update({unit: []})
    for item in data:
        book_name = item['book_name']
        unit = item['unit']
        classes = item['classes']
        res[book_name][unit].append(classes)
    return res


def word_list(request):
    queryset = models.Words.objects.all()
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
    }
    return render(request, 'words.html', context)
