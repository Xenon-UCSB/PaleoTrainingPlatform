# Generated by Django 3.0.3 on 2020-04-22 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_auto_20200327_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healingscore',
            name='score',
            field=models.CharField(max_length=3),
        ),
    ]
