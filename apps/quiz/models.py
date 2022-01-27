from datetime import datetime
from django.db import models
from apps.account.models import User
from apps.word.models import Book, Unit, Lesson, Word


class Quiz(models.Model):
    description = models.CharField(blank=False, max_length=200, verbose_name=u"描述")
    author = models.ForeignKey(User, verbose_name=u"用户", on_delete=models.CASCADE)
    lesson = models.CharField(verbose_name='课次', max_length=64)
    amount = models.IntegerField(verbose_name='题目数量', default=0)
    max_total_time = models.IntegerField(default=7200, verbose_name=u"最大总答题时间（秒）")
    max_word_time = models.IntegerField(default=120, verbose_name=u"单词最大答题时间（秒）")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.description


class QuizLog(models.Model):
    user = models.ForeignKey(User, verbose_name=u"用户", on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, verbose_name=u"测试", on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now, verbose_name=u"开始时间")
    finish_time = models.DateTimeField(null=True, verbose_name=u"完成时间")
    amount = models.IntegerField(verbose_name='题目总数')
    correct_count = models.IntegerField(default=0, verbose_name=u"答对题数")

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return "{0} - {1}".format(self.user.username, self.quiz.description)

    def correct_rate(self):
        return '%.2f%s' % (self.correct_count / self.amount, '%')


class QuizLogErr(models.Model):
    quiz = models.ForeignKey(Quiz, verbose_name=u"测试", on_delete=models.CASCADE)
    word = models.ForeignKey(Word, verbose_name=u"单词", on_delete=models.CASCADE)
    wrong = models.CharField(verbose_name='错误记录', max_length=64)
