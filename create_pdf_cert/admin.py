from django.contrib import admin
from .models import Cert

@admin.register(Cert)
class CertAdmin(admin.ModelAdmin):
    list_filter = ('date', 'name', 'course',)
    list_display = ('name', 'course', 'date',)
