# Generated by Django 4.1.6 on 2023-02-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Java',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='test', max_length=20, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Данные')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
        ),
    ]
