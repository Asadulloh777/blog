# Generated by Django 4.0.6 on 2022-08-16 09:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0008_remove_bolimlar_href'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bolimlar',
        ),
        migrations.RenameField(
            model_name='bolim',
            old_name='tur',
            new_name='icon',
        ),
        migrations.AddField(
            model_name='bolim',
            name='nom',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]