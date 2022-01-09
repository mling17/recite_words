from django.db import models


# Create your models here.
class User(models.Model):
    gender_choice = (
        (0, "男"),
        (1, "女"),
        (2, "未知")
    )
    level_choice = (
        (0, "普通用户"),
        (1, "高级用户")
    )
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=32)
    email = models.EmailField(verbose_name='邮箱', blank=True, null=True)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choice, default=3)
    level = models.SmallIntegerField(verbose_name='用户等级', default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    # has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.username
