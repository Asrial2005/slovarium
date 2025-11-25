from django.contrib import admin
from .models import Term

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ['word', 'created_at']
    search_fields = ['word', 'definition']