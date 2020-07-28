# Generated by Django 3.0.3 on 2020-06-21 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry_app', '0009_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client_Id', models.IntegerField()),
                ('First_Name', models.CharField(default='', max_length=50)),
                ('Last_Name', models.CharField(default='', max_length=50)),
                ('Address', models.CharField(default='', max_length=80)),
                ('Subscription_Package', models.CharField(default='', max_length=30)),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=255, unique=True)),
                ('Password', models.CharField(default='', max_length=50)),
                ('Conform_Password', models.CharField(default=' ', max_length=50)),
            ],
        ),
    ]
