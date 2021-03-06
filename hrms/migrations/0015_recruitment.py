# Generated by Django 4.0.5 on 2022-06-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0014_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('position', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=25)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
    ]
