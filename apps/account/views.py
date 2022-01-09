from io import BytesIO
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.db.models import Q
from apps.account.forms.account import RegisterModelForm, LoginForm
from apps.account import models
from apps.account.utils.image_code import check_code


# Create your views here.
def index(request):
    return HttpResponse('Test comment.')


def register(request):
    """注册视图"""
    if request.method == 'GET':
        form = RegisterModelForm(request)
        return render(request, 'register.html', {'form': form})
    form = RegisterModelForm(request, request.POST)
    if form.is_valid():
        form.save()
        return redirect('account:index')
        # return JsonResponse({"status": True, 'data': "/index/"})
    return render(request, 'register.html', {'form': form})


def login(request):
    """ 用户名和密码登录 """
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request, 'login.html', {'form': form})
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user_object = models.User.objects.filter(Q(username=username) | Q(mobile_phone=username) | Q(email=username)) \
            .filter(password=password).first()
        if user_object:
            request.session['user_id'] = user_object.id
            request.session.set_expiry(settings.SESSION_EXPIRE)
            return redirect(settings.SIGNED_DIRECT)
        form.add_error('username', '用户名或密码错误')

    return render(request, 'login.html', {'form': form})


def image_code(request):
    """ 生成图片验证码 """
    image_object, code = check_code()
    request.session['image_code'] = code
    request.session.set_expiry(60)  # 主动修改session的过期时间为60s
    stream = BytesIO()
    image_object.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    request.session.flush()
    return redirect(settings.SIGNED_DIRECT)
