# Generated by Django 3.2.11 on 2022-01-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0004_auto_20220121_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='symbol',
            field=models.CharField(max_length=64, verbose_name='音标'),
        ),
        migrations.AlterField(
            model_name='word',
            name='voice',
            field=models.FileField(upload_to='media/upload', verbose_name='读音'),
        ),
    ]
