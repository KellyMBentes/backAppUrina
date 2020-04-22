# Generated by Django 2.1.15 on 2020-04-22 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='questionform',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='option',
            name='formId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.QuestionForm'),
        ),
    ]
