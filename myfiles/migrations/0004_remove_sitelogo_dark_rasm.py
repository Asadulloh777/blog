# Generated by Django 4.0.6 on 2022-08-05 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0003_sitelogo_rename_bolimlar_postlar_bolimlar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitelogo',
            name='dark_rasm',
        ),
    ]
