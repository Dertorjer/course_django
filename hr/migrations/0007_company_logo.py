# Generated by Django 5.0.6 on 2024-07-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_employee_avatar_employee_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
    ]
