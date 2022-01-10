DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jp_words',
        'USER': 'root',
        'PASSWORD': 'mling17@163.com',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# ########### 登录白名单：无需登录就可以访问的页面 ###########
WHITE_REGEX_URL_LIST = [
    "/account/regist/",
    "/account/login/",
    "/account/image/code/",
    "/account/index/",
]
# 登录承购后的跳转页面,namespace:name
SIGNED_DIRECT = 'manage:index'
# session过期时间，默认14天
SESSION_EXPIRE = 60 * 60 * 24 * 14
