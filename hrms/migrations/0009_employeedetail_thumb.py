# Generated by Django 4.0.5 on 2022-06-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0008_employeedetail_first_name_employeedetail_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetail',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
