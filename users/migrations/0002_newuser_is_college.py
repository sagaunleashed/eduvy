# Generated by Django 3.0.5 on 2021-06-24 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='is_college',
            field=models.BooleanField(default=False),
        ),
    ]
