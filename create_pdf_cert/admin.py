from django.contrib import admin
from .models import Cert

@admin.register(Cert)
class CertAdmin(admin.ModelAdmin):
    list_filter = ('date', 'course',)
    list_display = ('name', 'course', 'date',)
