# Generated by Django 4.1.5 on 2023-02-09 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Css',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название темы')),
                ('text', models.TextField(verbose_name='Данные')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
        ),
    ]
