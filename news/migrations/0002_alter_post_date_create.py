# Generated by Django 4.2.1 on 2023-06-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_create',
            field=models.DateField(auto_now_add=True),
        ),
    ]
