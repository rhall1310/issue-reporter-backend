from django.contrib import admin
from .models import Report

# Register your models here.
class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        ("User Info", {"fields": ["title", "first_name", "last_name"]}),
        ("Report Details", {"fields": ["category", "details"]}),
        ("Location Details", {"fields": ["easting", "northing", "address"]}),
    ]


admin.site.site_header = "Issue Reporter Admin"

admin.site.register(Report, ReportAdmin)
