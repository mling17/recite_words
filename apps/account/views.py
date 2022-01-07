from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms.forms import RegisterForm, LoginForm
from apps.account import models
from utiles import tools


# Create your views here.
def index(request):
    return HttpResponse('Test comment.')


def register(request):
    """注册视图"""
    if request.session.get('is_login', None):
        # 登录状态不允许注册
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            email = register_form.cleaned_data['email']
            new_user = models.User()
            new_user.username = username
            new_user.password = tools.hash_md5(password)  # 使用加密密码
            new_user.email = email
            new_user.save()
            print(username)
            return redirect(reverse('account:login'))  # 自动跳转到登录页面
        else:
            return render(request, 'register.html', locals())
    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('index')))
        else:
            return render(request, 'login.html', {'login_form': login_form})
    login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('index')))
        else:
            print(3333333333)
            return render(request, 'login.html', {"login_form": login_form})
    else:
        login_form = LoginForm()
    context = dict()
    context['login_form'] = login_form
    return render(request, 'login.html', context)
