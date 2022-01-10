from django.shortcuts import render, HttpResponse
from apps.word import models
from utils.pagination import Pagination


# Create your views here.
def word_list(request):
    queryset = models.Words.objects.all()
    page_object = Pagination(
        current_page=request.GET.get('page'),
        all_count=queryset.count(),
        base_url=request.path_info,
        query_params=request.GET
    )
    words_obj_list = queryset[page_object.start:page_object.end]
    context = {
        'word_object_list': words_obj_list,
        'page_html': page_object.page_html()
    }
    return render(request, 'words.html', context)
