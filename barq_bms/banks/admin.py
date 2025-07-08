from django.contrib import admin
from banks.models import Branch, Bank

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'is_islamic']
    list_filter = ['is_islamic']


@admin.register(Branch)
class BankAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'bank']
    list_filter = ['bank']
