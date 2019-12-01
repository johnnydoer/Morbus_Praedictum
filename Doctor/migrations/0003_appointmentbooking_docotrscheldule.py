# Generated by Django 2.2.7 on 2019-11-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_auto_20191105_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointmentBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docUsername', models.CharField(max_length=40)),
                ('day', models.CharField(max_length=10)),
                ('slotTime', models.TimeField()),
                ('patientUsername', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='docotrScheldule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docUsername', models.CharField(max_length=40)),
                ('day', models.CharField(max_length=10)),
                ('interval', models.IntegerField(choices=[(15, '10 min'), (20, '10 min'), (30, '30 min'), (60, '60 min')], default='--choose interval--')),
                ('openTime', models.TimeField()),
                ('closeTime', models.TimeField()),
            ],
        ),
    ]