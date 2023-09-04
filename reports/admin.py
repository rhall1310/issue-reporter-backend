from django.contrib import admin
from .models import Report

# Register your models here.
class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Report Details",
            {
                "fields": [
                    "category",
                    "details",
                ]
            },
        ),
        ("Location Details", {"fields": ["lat", "lon", "address"]}),
        ("Report Details", {"fields": ["resolved", "photo"]}),
        (
            "User Info",
            {"fields": ["title", "first_name", "last_name", "email", "phone_number"]},
        ),
    ]


admin.site.site_header = "Issue Reporter Admin"

admin.site.register(Report, ReportAdmin)
