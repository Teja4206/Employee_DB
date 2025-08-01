# Generated by Django 5.2.4 on 2025-07-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Designation',
            field=models.ImageField(upload_to='employee_photos/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Email_address',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Phone_number',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Photo',
            field=models.CharField(max_length=150),
        ),
    ]
