# Generated by Django 4.1.3 on 2022-12-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_pedido"),
    ]

    operations = [
        migrations.AddField(
            model_name="pedido",
            name="datetime",
            field=models.DateTimeField(auto_now_add=True, default='2022-10-23 10:30'),
            preserve_default=False,
        ),
    ]
