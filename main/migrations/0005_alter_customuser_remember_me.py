# Generated by Django 4.2.5 on 2023-10-27 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_customuser_remember_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='remember_me',
            field=models.BooleanField(null=True),
        ),
    ]
