# Generated by Django 2.2.11 on 2020-04-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalData', '0004_auto_20200414_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='addressCity',
            field=models.CharField(default=1, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldata',
            name='addressDistrict',
            field=models.CharField(default=1, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldata',
            name='addressFederalState',
            field=models.CharField(default=1, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldata',
            name='addressStreet',
            field=models.CharField(default=1, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldata',
            name='cep',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='gender',
            field=models.CharField(max_length=15),
        ),
    ]