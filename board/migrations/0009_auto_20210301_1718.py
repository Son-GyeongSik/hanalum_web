# Generated by Django 3.1.5 on 2021-03-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_board_visible_anonymous'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='default_board_format',
        ),
        migrations.AddField(
            model_name='board',
            name='board_format_category',
            field=models.CharField(choices=[('text', '텍스트 중심'), ('gallery', '이미지 중심')], default='text', max_length=10, verbose_name='게시판 기본 형태'),
        ),
    ]
