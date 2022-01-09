app(account),用来做用户认证
1. 总url.py添加account 的路由
from django.urls import path, re_path
import apps.account.views as views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('regist/', views.register, name='regist'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    re_path(r'image/code/$', views.image_code, name='image_code'),
]

2. settings.py
添加middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.account.middleware.auth.AuthMiddleware',
]
添加白名单

########### 登录白名单：无需登录就可以访问的页面

WHITE_REGEX_URL_LIST = [
    "/account/regist/",
    "/account/login/",
    "/account/image/code/",
    "/account/index/",
]
添加msql数据库
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jp_words',
        'USER': 'root',
        'PASSWORD': 'mling17!163.com',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
修改登录成功后的跳转地址
登录承购后的跳转页面

```
# 登录承购后的跳转页面,namespace:name
SIGNED_DIRECT = 'manage:index'
```

修改session过期时间
session过期时间，默认14天

SESSION_EXPIRE = 60 * 60 * 24 * 14



