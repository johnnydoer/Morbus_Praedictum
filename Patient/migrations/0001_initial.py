# Generated by Django 2.2.4 on 2019-12-07 17:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('Address_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Home', models.CharField(max_length=250)),
                ('Street', models.CharField(max_length=250)),
                ('Pin', models.CharField(default=0, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('Patient_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Patient_First_Name', models.CharField(max_length=200)),
                ('Patient_Last_Name', models.CharField(max_length=200)),
                ('Patient_Phone_Number', phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None)),
                ('Patient_Picture', models.ImageField(default='default-user-image.jpg', null=True, upload_to='media')),
                ('Patient_Gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Transgender'), (4, 'Other')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('Patient_DOB', models.DateField(max_length=8)),
                ('Patient_Blood_Group', models.IntegerField(choices=[(1, 'A+'), (2, 'A-'), (3, 'B+'), (4, 'B-'), (5, 'O+'), (6, 'O-'), (7, 'AB+'), (8, 'AB-')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('Patient_Blood_Donation', models.IntegerField(choices=[(0, 'Yes'), (1, 'No')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Patient_Email', models.EmailField(max_length=254)),
                ('Patient_Address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Patient.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.City')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Patient.Area'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Patient.City'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
