# Generated by Django 4.0.6 on 2022-08-08 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0007_bolimlar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bolimlar',
            name='href',
        ),
    ]
