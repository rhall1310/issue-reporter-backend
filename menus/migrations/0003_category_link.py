# Generated by Django 4.0.6 on 2022-07-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='link',
            field=models.CharField(default='SOME STRING', max_length=120),
        ),
    ]
