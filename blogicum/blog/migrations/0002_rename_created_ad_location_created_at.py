# Generated by Django 3.2.16 on 2024-11-28 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='created_ad',
            new_name='created_at',
        ),
    ]