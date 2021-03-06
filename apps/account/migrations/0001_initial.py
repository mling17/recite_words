# Generated by Django 3.2.11 on 2022-01-08 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('mobile_phone', models.CharField(max_length=32, verbose_name='手机号')),
                ('gender', models.SmallIntegerField(choices=[(0, '男'), (1, '女'), (2, '未知')], default=3, verbose_name='性别')),
                ('level', models.SmallIntegerField(default=0, verbose_name='用户等级')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
    ]
