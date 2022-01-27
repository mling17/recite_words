"""recite_words URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
import apps.quiz.views as views

urlpatterns = [
    # path('index/', views.index, name='index'),
    # path('list/', views.word_list, name='word_list'),
    path('list/', views.quiz, name='quiz_list'),
    path('create/', views.quiz_create, name='quiz_create'),
    path('start/<int:q_id>/', views.quiz_start, name='quiz_start'),
    path('result/<int:q_id>/', views.quiz_result, name='quiz_result'),
    path('get_quiz_question/', views.get_quiz_question, name='get_quiz_question')
]
