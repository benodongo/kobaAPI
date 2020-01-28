from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$',
                                  message="Phone number must be entered in the format :'+999999999999'. upto 12 digits allowed")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    id_number = models.CharField(max_length=200, null=True)
    dob = models.DateField(
        max_length=10,
        help_text="format : YYYY-MM-DD",
        null=True)
    gender_choices = [('Male', 'Male'), ('Female', 'Female')]
    gender = models.CharField(
        choices=gender_choices,
        max_length=6,
        default=None,
        null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_mobile = models.BooleanField(default=False)
    is_individual = models.BooleanField(default=True)
    is_business = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


