# Generated by Django 5.0.6 on 2024-07-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0002_power_gamecarecter_alter_power_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='power',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='C:\\Users\\abdo7\\OneDrive\\Bureau\\hollow-4\\venv\\crud\\static/images/upload'),
        ),
    ]
