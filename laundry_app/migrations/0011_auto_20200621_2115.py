# Generated by Django 3.0.3 on 2020-06-21 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry_app', '0010_clientdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientdetail',
            name='id',
        ),
        migrations.AlterField(
            model_name='clientdetail',
            name='Client_Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
