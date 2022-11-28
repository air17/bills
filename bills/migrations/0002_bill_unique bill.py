# Generated by Django 4.1.3 on 2022-11-28 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bills", "0001_initial"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="bill",
            constraint=models.UniqueConstraint(
                fields=("client_name", "client_org", "number"), name="unique bill"
            ),
        ),
    ]