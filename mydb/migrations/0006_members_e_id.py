# Generated by Django 4.2.7 on 2023-12-02 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mydb', '0005_rename_emplyoee_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='e_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='mydb.employee'),
            preserve_default=False,
        ),
    ]
