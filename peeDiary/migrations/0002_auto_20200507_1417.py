# Generated by Django 2.2.11 on 2020-05-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peeDiary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peediary',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]