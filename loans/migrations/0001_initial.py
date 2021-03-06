# Generated by Django 3.0.2 on 2020-01-09 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('approved_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('issued_date', models.DateField(null=True)),
                ('due_date', models.DateField(null=True)),
                ('interest', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('period', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('0', 'Pending Approval'), ('1', 'Approved'), ('2', 'Disbursed'), ('3', 'Repayed'), ('4', 'Defaulted'), ('5', 'Written Off')], default=None, max_length=1, null=True)),
                ('loan_serial', models.CharField(max_length=255, null=True)),
                ('application_serial', models.CharField(max_length=255, null=True)),
                ('applicant', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
