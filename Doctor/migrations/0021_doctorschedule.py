# Generated by Django 2.2.7 on 2019-11-15 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0020_delete_doctorschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctorSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docUsername', models.CharField(max_length=40)),
                ('day', models.CharField(max_length=10)),
                ('interval', models.IntegerField(choices=[(10, '10 min'), (15, '15 min'), (20, '20 min'), (30, '30 min'), (60, '60 min')], default='10')),
                ('openTime', models.TimeField(choices=[(datetime.time(0, 0), '00:00'), (datetime.time(1, 0), '01:00'), (datetime.time(2, 0), '02:00'), (datetime.time(3, 0), '03:00'), (datetime.time(4, 0), '04:00'), (datetime.time(5, 0), '05:00'), (datetime.time(6, 0), '06:00'), (datetime.time(7, 0), '07:00'), (datetime.time(8, 0), '08:00'), (datetime.time(9, 0), '09:00'), (datetime.time(10, 0), '10:00'), (datetime.time(11, 0), '11:00'), (datetime.time(12, 0), '12:00'), (datetime.time(13, 0), '13:00'), (datetime.time(14, 0), '14:00'), (datetime.time(15, 0), '15:00'), (datetime.time(16, 0), '16:00'), (datetime.time(17, 0), '17:00'), (datetime.time(18, 0), '18:00'), (datetime.time(19, 0), '19:00'), (datetime.time(20, 0), '20:00'), (datetime.time(21, 0), '21:00'), (datetime.time(22, 0), '22:00'), (datetime.time(23, 0), '23:00')])),
                ('closeTime', models.TimeField(choices=[(datetime.time(0, 0), '00:00'), (datetime.time(1, 0), '01:00'), (datetime.time(2, 0), '02:00'), (datetime.time(3, 0), '03:00'), (datetime.time(4, 0), '04:00'), (datetime.time(5, 0), '05:00'), (datetime.time(6, 0), '06:00'), (datetime.time(7, 0), '07:00'), (datetime.time(8, 0), '08:00'), (datetime.time(9, 0), '09:00'), (datetime.time(10, 0), '10:00'), (datetime.time(11, 0), '11:00'), (datetime.time(12, 0), '12:00'), (datetime.time(13, 0), '13:00'), (datetime.time(14, 0), '14:00'), (datetime.time(15, 0), '15:00'), (datetime.time(16, 0), '16:00'), (datetime.time(17, 0), '17:00'), (datetime.time(18, 0), '18:00'), (datetime.time(19, 0), '19:00'), (datetime.time(20, 0), '20:00'), (datetime.time(21, 0), '21:00'), (datetime.time(22, 0), '22:00'), (datetime.time(23, 0), '23:00')])),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
    ]