# Generated by Django 3.1.5 on 2021-01-24 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_category",
            field=models.CharField(
                choices=[
                    ("2014(1기)", "2014(1기)"),
                    ("2015(2기)", "2015(2기)"),
                    ("2016(3기)", "2016(3기)"),
                    ("2017(4기)", "2017(4기)"),
                    ("2018(5기)", "2018(5기)"),
                    ("2019(6기)", "2019(6기)"),
                    ("2020(7기)", "2020(7기)"),
                    ("2021(8기)", "2021(8기)"),
                    ("교직원", "교직원"),
                    ("외부인", "외부인"),
                    ("한아름", "한아름"),
                    ("관리자", "관리자"),
                ],
                max_length=10,
                verbose_name="유저 카테고리",
            ),
        ),
    ]
