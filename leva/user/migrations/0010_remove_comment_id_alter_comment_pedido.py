# Generated by Django 4.1.3 on 2022-12-02 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0009_rename_body_comment_review"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="id",
        ),
        migrations.AlterField(
            model_name="comment",
            name="pedido",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="user.pedido",
            ),
        ),
    ]