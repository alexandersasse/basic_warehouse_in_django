# Generated by Django 4.2 on 2023-04-04 12:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("stock", "0007_comment_alter_post_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="comment",
        ),
    ]
