# Generated by Django 3.0.2 on 2020-01-15 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=None, max_length=6, null=True),
        ),
    ]