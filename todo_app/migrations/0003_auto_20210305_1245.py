# Generated by Django 3.1.5 on 2021-03-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_auto_20210305_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
