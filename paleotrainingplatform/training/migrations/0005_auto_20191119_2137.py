# Generated by Django 2.1.5 on 2019-11-19 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_auto_20191015_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesionimage',
            name='lesion_type',
            field=models.CharField(max_length=256),
        ),
    ]
