# Generated by Django 4.1.3 on 2022-12-02 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_pedido_datetime"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("body", models.CharField(max_length=255)),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("score", models.IntegerField(default=0)),
                (
                    "pedido",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="user.pedido"
                    ),
                ),
            ],
        ),
    ]