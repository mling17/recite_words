from django.db import models


class Classify(models.Model):
    name = models.CharField(verbose_name='名称', max_length=32)
    description = models.CharField(verbose_name='描述', blank=True, null=True, max_length=32)
    type = models.SmallIntegerField(verbose_name='类型', choices=((1, '书名'), (2, '单元'), (1, '课次')))
    c_id = models.ForeignKey(verbose_name='关联的上级分类', to='Classify', null=True, blank=True, related_name='parents',
                             on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Words(models.Model):
    word = models.CharField(verbose_name='外语单词', max_length=32)
    symbol = models.CharField(verbose_name='音标', max_length=64)
    voice = models.CharField(verbose_name='读音', max_length=32)
    cn = models.CharField(verbose_name='中文释义', max_length=64)
    word_type = models.CharField(verbose_name='词性', max_length=16)
    sentence = models.CharField(verbose_name='例句', max_length=512)


class WordClassify(models.Model):
    c_id = models.ForeignKey(verbose_name='分类', to='Classify', on_delete=models.CASCADE)
    w_id = models.ForeignKey(verbose_name='单词', to='WordClassify', on_delete=models.CASCADE)
