# Generated by Django 3.0.3 on 2020-07-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry_app', '0017_auto_20200712_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('htmlupload', models.FileField(upload_to='')),
                ('formupload', models.FileField(upload_to='')),
                ('modelupload', models.FileField(upload_to='upload_file')),
            ],
        ),
    ]
