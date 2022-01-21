import json
from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe
from django.db.models import Count
from apps.word import models
from utils.pagination import Pagination
from utils.tool import get_word_catalog
from apps.stark.service.v1 import StarkHandler


def word_list(request):
    if request.method == 'GET':
        queryset = models.Word.objects.all()
        page_object = Pagination(
            current_page=request.GET.get('page'),
            all_count=queryset.count(),
            base_url=request.path_info,
            query_params=request.GET
        )
        words_obj_list = queryset[page_object.start:page_object.end]
        context = {
            'word_object_list': words_obj_list,
            'page_html': page_object.page_html(),
            'column_names': [],
            'query_params': {'book_name': book, 'unit': unit, 'lesson': lesson}
        }
        return render(request, 'words.html', context)


def word_test(request):
    return render(request, 'learn_start.html')


class WordHandler(StarkHandler):
    list_display = ['word', 'symbol', 'cn', 'word_type', 'sentence']
    # search_group = ['lesson']
    search_list = ['word', 'symbol', 'cn']
