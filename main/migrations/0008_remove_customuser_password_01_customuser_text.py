# Generated by Django 4.2.5 on 2023-10-15 19:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_merge_20231015_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='password_01',
        ),
        migrations.AddField(
            model_name='customuser',
            name='text',
            field=models.CharField(default=0, max_length=50, validators=[django.core.validators.EmailValidator('test')]),
            preserve_default=False,
        ),
    ]
