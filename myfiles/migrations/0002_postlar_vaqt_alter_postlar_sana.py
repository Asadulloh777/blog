# Generated by Django 4.0.6 on 2022-07-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlar',
            name='vaqt',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='postlar',
            name='sana',
            field=models.DateField(auto_now=True),
        ),
    ]
