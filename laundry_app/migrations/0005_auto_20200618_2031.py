# Generated by Django 3.0.3 on 2020-06-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry_app', '0004_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category_name',
            new_name='Catogory_name',
        ),
        migrations.RenameField(
            model_name='item_detail',
            old_name='Category',
            new_name='Catogory',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]