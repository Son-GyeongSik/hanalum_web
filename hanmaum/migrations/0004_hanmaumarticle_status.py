# Generated by Django 3.1.5 on 2021-02-02 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanmaum', '0003_auto_20210202_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='hanmaumarticle',
            name='status',
            field=models.CharField(choices=[('d', 'draft'), ('p', 'published'), ('t', 'trash')], default='d', max_length=2, verbose_name='게시글 공개 상태'),
        ),
    ]
