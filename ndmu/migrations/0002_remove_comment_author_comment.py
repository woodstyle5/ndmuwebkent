# Generated by Django 2.1.3 on 2018-12-28 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ndmu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author_comment',
        ),
    ]
