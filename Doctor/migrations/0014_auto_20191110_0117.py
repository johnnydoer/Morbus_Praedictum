# Generated by Django 2.2.7 on 2019-11-09 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0013_auto_20191110_0031'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='docotrscheldule',
            table='schedule',
        ),
    ]