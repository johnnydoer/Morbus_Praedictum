# Generated by Django 2.2.7 on 2019-11-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscellaneous', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]