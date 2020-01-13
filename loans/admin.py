from django.contrib import admin
from .models import Loan

# Register your models here.


class LoanAdmin(admin.ModelAdmin):
    list_display = ('user', 'requested_amount', 'approved_amount', 'issued_date', 'due_date', 'interest', 'period', 'status', 'loan_serial')
    list_display_links = ('user',)
    list_filter = ('user',)
    list_editable = ('status',)
    search_fields = ('user','due_date')
    list_per_page = 25

admin.site.register(Loan, LoanAdmin)