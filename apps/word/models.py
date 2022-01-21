from django.db import models


class Base(models.Model):
    description = models.CharField(verbose_name='描述', max_length=255, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Book(Base):
    name = models.CharField(verbose_name='书本名称', max_length=32)

    def unit_count(self):
        pass

    def __str__(self):
        return self.name


class Unit(Base):
    name = models.CharField(verbose_name='单元名称', max_length=32)
    book = models.ForeignKey(verbose_name='书本', to='Book', on_delete=models.CASCADE)

    def learn_count(self):
        pass

    def review_count(self, user_id):
        pass

    def lesson_count(self):
        pass

    def __str__(self):
        return self.name


class Lesson(Base):
    name = models.CharField(verbose_name='课次名称', max_length=32)
    unit = models.ForeignKey(verbose_name='单元', to='Unit', on_delete=models.CASCADE)

    def learn_count(self):
        pass

    def review_count(self, user_id):
        pass

    def word_count(self):
        pass

    def __str__(self):
        return self.name


class Word(models.Model):
    lesson = models.ForeignKey(verbose_name='课次', to='Lesson', on_delete=models.CASCADE)
    word = models.CharField(verbose_name='外语单词', max_length=64)
    symbol = models.CharField(verbose_name='音标', max_length=64)
    voice = models.FileField(verbose_name='读音', upload_to='media/upload')
    cn = models.CharField(verbose_name='中文释义', max_length=64)
    word_type = models.CharField(verbose_name='词性', max_length=32)
    sentence = models.CharField(verbose_name='例句', max_length=512)

    def __str__(self):
        return f'{self.word}|{self.cn}'

    def cat(self):
        book = self.lesson.unit.book.name
        unit = self.lesson.unit.name
        lesson = self.lesson.name
        return f'{book}|{unit}|{lesson}'
