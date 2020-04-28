# Generated by Django 2.2.11 on 2020-04-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalData', '0007_auto_20200414_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='birthPlace',
            field=models.CharField(default='', max_length=55),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='civilStatus',
            field=models.CharField(default='', max_length=55),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='ethnicity',
            field=models.CharField(default='', max_length=55),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='familyIncome',
            field=models.CharField(default='', max_length=55),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='occupation',
            field=models.CharField(default='', max_length=55),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='schooling',
            field=models.CharField(default='', max_length=55),
        ),
    ]