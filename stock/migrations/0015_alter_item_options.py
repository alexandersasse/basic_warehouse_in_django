# Generated by Django 4.2 on 2023-04-04 22:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("stock", "0014_author_comment_post"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"managed": False, "ordering": ["date_of_stock"]},
        ),
    ]
