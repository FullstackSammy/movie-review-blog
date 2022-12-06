# Generated by Django 3.2.16 on 2022-12-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('Horror', 'Horror'), ('Comedy', 'Comedy'), ('Sci-fi', 'Sci-fi'), ('Fantasy', 'Fantasy'), ('Action', 'Action'), ('Romantic', 'Romantic'), ('Thriller', 'Thriller'), ('Anime', 'Anime'), ('Other', 'Other')], default='Horror', max_length=50),
        ),
    ]
