# Generated by Django 5.0.7 on 2024-07-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0009_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='name',
            field=models.CharField(default=200, max_length=200),
            preserve_default=False,
        ),
    ]
