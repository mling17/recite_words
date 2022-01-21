from django.contrib import admin
from apps.word import models

# Register your models here.
admin.site.register(models.Book)
admin.site.register(models.Unit)
admin.site.register(models.Lesson)
admin.site.register(models.Word)
