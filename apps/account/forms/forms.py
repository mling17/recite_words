from django import forms
from apps.account import models
from django.contrib import auth
from utiles import tools


# from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # captcha = CaptchaField(label='验证码')
    # def clean(self):
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password']
    #     # user = auth.authenticate(username=username, password=tools.hash_md5(password))
    #     user = models.User.objects.filter(username=username, password=tools.hash_md5(password)).exists()
    #     raise forms.ValidationError('用户名或密码错误')
    #     if not user:
    #         print(11111)
    #         raise forms.ValidationError('用户名或密码错误')
    #     else:
    #         self.cleaned_data['user'] = user
    #     return self.cleaned_data
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not models.User.objects.filter(username=username, password=tools.hash_md5(password)).exists():
            raise forms.ValidationError('asdfas')
        return self.cleaned_data


class RegisterForm(forms.Form):
    gender_choice = (
        (0, "男"),
        (1, "女"),
        (2, "保密"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TimeInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_check = forms.CharField(label="确认密码", max_length=256,
                                     widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    # gender = forms.ChoiceField(label='性别', choices=gender_choice)

    # captcha = CaptchaField(label='验证码')
    def clean_password_check(self):
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']
        if password != password_check:
            raise forms.ValidationError('两次输入的密码不一致')
        return password_check

    def clean_username(self):
        username = self.cleaned_data['username']
        if models.User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已注册')
        return username
