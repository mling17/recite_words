from django.shortcuts import render, HttpResponse
from apps.word import models


# Create your views here.
def word_list(request):
    words = models.Words.objects.all()
    return render(request, 'words.html', {'words': words})
