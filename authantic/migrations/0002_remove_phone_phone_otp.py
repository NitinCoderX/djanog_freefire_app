# Generated by Django 4.0.2 on 2022-02-26 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authantic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='phone_otp',
        ),
    ]