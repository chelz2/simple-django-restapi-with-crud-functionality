# Generated by Django 4.2 on 2024-08-19 21:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_alter_blogpost_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
