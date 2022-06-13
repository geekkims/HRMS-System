# Generated by Django 4.0.5 on 2022-06-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0002_department_remove_employeedetail_empdept_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetail',
            name='emergency',
            field=models.CharField(default='10:19', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeedetail',
            name='personalemail',
            field=models.EmailField(default='test@gmail.com', max_length=125),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeedetail',
            name='workemail',
            field=models.EmailField(default='test@gmail.com', max_length=125),
            preserve_default=False,
        ),
    ]