# Generated by Django 2.2.11 on 2020-04-13 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='phone',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personalData.Phone'),
        ),
    ]
