# Generated by Django 4.2.7 on 2023-11-25 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydb', '0003_rename_admin_admindb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='admindb',
            new_name='adminlogin',
        ),
    ]
