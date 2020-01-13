from django.contrib import admin
from .models import userProfile

# Register your models here.

class userProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number','id_number', 'dob', 'gender')
    list_display_links = ('user',)
    list_filter = ('user',)
    search_fields = ('user',)
    list_per_page = 25



admin.site.register(userProfile, userProfileAdmin)