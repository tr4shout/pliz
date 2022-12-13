# Generated by Django 4.1.3 on 2022-11-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Uni",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tittle", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="")),
                ("title_ref", models.TextField()),
                ("ref", models.URLField()),
            ],
        ),
    ]
