# Generated by Django 4.2.7 on 2023-11-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
