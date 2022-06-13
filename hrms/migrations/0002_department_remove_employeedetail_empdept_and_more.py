# Generated by Django 4.0.5 on 2022-06-13 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('history', models.TextField(blank=True, default='No History', max_length=1000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employeedetail',
            name='empdept',
        ),
        migrations.RemoveField(
            model_name='employeedetail',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='employeedetail',
            name='user',
        ),
        migrations.AddField(
            model_name='employeedetail',
            name='address',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='employeedetail',
            name='mobile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employeedetail',
            name='joiningdate',
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name='Kin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=100)),
                ('occupation', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=15)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hrms.employeedetail')),
            ],
        ),
        migrations.AddField(
            model_name='employeedetail',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrms.department'),
        ),
    ]