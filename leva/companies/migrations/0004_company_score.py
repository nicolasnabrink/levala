# Generated by Django 4.1.2 on 2022-11-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_alter_company_job_alter_company_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]