from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Loan(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        default=None,
        on_delete=models.CASCADE,
        related_name='user'
    )
    requested_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    approved_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    issued_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    interest = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    period = models.IntegerField(null=True)
    loan_status = [('0','Pending Approval'), ('1','Approved'), ('2','Disbursed'), ('3', 'Repayed'), ('4', 'Defaulted'),
                   ('5','Written Off')]
    status = models.CharField(
        choices=loan_status,
        max_length=1,
        default=None,
        null=True
    )
    loan_serial = models.CharField(max_length=255, null=True)
    application_serial = models.CharField(max_length=255, null=True)
