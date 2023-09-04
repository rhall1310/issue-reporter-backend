from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            "id",
            "category",
            "address",
            "details",
            "photo",
            "lat",
            "lon",
            "title",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        )
