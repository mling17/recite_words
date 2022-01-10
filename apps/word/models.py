from django.db import models


# Create your models here.
class Words(models.Model):
    book_name = models.CharField(verbose_name='书本名称', max_length=32)
    unit = models.SmallIntegerField(verbose_name='单元')
    classes = models.SmallIntegerField(verbose_name='课次')
    word = models.CharField(verbose_name='外语单词', max_length=32)
    symbol = models.CharField(verbose_name='音标', max_length=64)
    voice = models.CharField(verbose_name='读音', max_length=32)
    cn = models.CharField(verbose_name='中文释义', max_length=64)
    word_type = models.CharField(verbose_name='词性', max_length=16)
    sentence = models.CharField(verbose_name='例句', max_length=512)
