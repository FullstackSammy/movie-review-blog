# Generated by Django 3.2.16 on 2022-12-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='placeholder', max_length=200, unique=True),
        ),
    ]