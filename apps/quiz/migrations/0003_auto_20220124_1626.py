# Generated by Django 3.2.11 on 2022-01-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20220124_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='book',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='unit',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='lesson',
            field=models.CharField(max_length=64, verbose_name='课次'),
        ),
    ]
