# Generated by Django 4.0.6 on 2023-01-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_report_email_report_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='resolved',
            field=models.BooleanField(null=True),
        ),
    ]
