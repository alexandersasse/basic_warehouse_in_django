# Generated by Django 4.2 on 2023-04-04 14:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("stock", "0012_alter_post_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
        migrations.RemoveField(
            model_name="post",
            name="comment",
        ),
        migrations.DeleteModel(
            name="Author",
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
        migrations.DeleteModel(
            name="Post",
        ),
    ]
