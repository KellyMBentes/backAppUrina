# Generated by Django 2.1.15 on 2020-04-22 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('birthDate', models.DateField()),
                ('gender', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=15)),
                ('rg', models.CharField(max_length=15)),
                ('cep', models.CharField(max_length=15)),
                ('addressNumber', models.CharField(max_length=15)),
                ('addressComplement', models.CharField(blank=True, max_length=55, null=True)),
                ('addressStreet', models.CharField(max_length=55)),
                ('addressCity', models.CharField(max_length=55)),
                ('addressDistrict', models.CharField(max_length=55)),
                ('addressFederalState', models.CharField(max_length=55)),
                ('healthEnsurance', models.BooleanField()),
                ('healthEnsuranceCompany', models.CharField(max_length=15)),
                ('healthEnsuranceDescription', models.CharField(max_length=15)),
                ('hasHealthData', models.BooleanField()),
                ('hasPersonalData', models.BooleanField(default=True)),
                ('hasPrescription', models.BooleanField()),
                ('hasQrMedication', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='personaldata',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalData.Phone'),
        ),
    ]
