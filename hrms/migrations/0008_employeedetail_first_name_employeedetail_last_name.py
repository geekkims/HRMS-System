# Generated by Django 4.0.5 on 2022-06-13 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0007_remove_employeedetail_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetail',
            name='first_name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeedetail',
            name='last_name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]