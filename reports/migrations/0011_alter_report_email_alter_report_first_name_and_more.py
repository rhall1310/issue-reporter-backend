# Generated by Django 4.0.6 on 2023-08-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_alter_report_resolved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='email',
            field=models.EmailField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='first_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='last_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='title',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
