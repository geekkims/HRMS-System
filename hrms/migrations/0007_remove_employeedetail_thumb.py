# Generated by Django 4.0.5 on 2022-06-13 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0006_rename_bankdetails_employeedetail_bank_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetail',
            name='thumb',
        ),
    ]
