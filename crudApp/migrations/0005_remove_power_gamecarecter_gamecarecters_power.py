# Generated by Django 5.0.6 on 2024-07-07 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0004_alter_gamecarecters_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='power',
            name='gameCarecter',
        ),
        migrations.AddField(
            model_name='gamecarecters',
            name='power',
            field=models.ManyToManyField(to='crudApp.power'),
        ),
    ]