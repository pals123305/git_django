# Generated by Django 3.1.5 on 2021-03-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='detail',
        ),
        migrations.AlterField(
            model_name='tasks',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
