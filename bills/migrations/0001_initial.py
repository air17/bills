# Generated by Django 4.1.3 on 2022-11-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bill",
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
                (
                    "client_name",
                    models.CharField(max_length=100, verbose_name="Client name"),
                ),
                (
                    "client_org",
                    models.CharField(
                        max_length=100, verbose_name="Client organization"
                    ),
                ),
                ("number", models.IntegerField(verbose_name="Bill number")),
                (
                    "sum",
                    models.DecimalField(
                        decimal_places=2, max_digits=12, verbose_name="Bill sum"
                    ),
                ),
                ("date", models.DateField(verbose_name="Date")),
                ("service", models.TextField(verbose_name="Service name")),
            ],
        ),
    ]