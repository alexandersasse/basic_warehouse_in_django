# Generated by Django 4.2 on 2023-04-26 21:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("stock", "0016_alter_item_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"managed": True},
        ),
    ]