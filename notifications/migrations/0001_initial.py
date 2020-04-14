# Generated by Django 2.2.11 on 2020-04-14 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isSelectedAll', models.BooleanField(default=True)),
                ('isPriority', models.BooleanField(default=False)),
                ('userId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isSelected', models.BooleanField(default=True)),
                ('isPriority', models.BooleanField(default=False)),
                ('text', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=55)),
                ('notificationId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifications.Notification')),
            ],
            options={
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
            },
        ),
    ]
