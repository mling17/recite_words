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
from django.contrib import admin
from django.urls import path, include, re_path
from apps.stark.service.v1 import site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(('apps.account.urls', 'account'), namespace='account')),
    path('manage/', include(('apps.management.urls', 'manage'), namespace='manage')),
    path('word/', include(('apps.word.urls', 'word'), namespace='word')),
    path('testing/', include(('apps.testing.urls', 'testing'), namespace='testing')),
]
