# Generated by Django 2.0.7 on 2019-04-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0003_auto_20190423_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='username',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='enter the valid username', max_length=50)),
                ('password', models.CharField(default='enter a valid password', max_length=50)),
            ],
        ),
    ]
