# Generated by Django 3.1.5 on 2021-03-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_anonymous_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='top_fixed',
            field=models.BooleanField(default=False, verbose_name='상단 고정 게시물'),
        ),
    ]
