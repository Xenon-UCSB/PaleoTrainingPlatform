# Generated by Django 3.0.2 on 2020-01-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0008_healingreference'),
    ]

    operations = [
        migrations.CreateModel(
            name='LesionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesion_type', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='lesionimage',
            name='lesion_type',
        ),
        migrations.AddField(
            model_name='lesionimage',
            name='lesion_types',
            field=models.ManyToManyField(to='training.LesionType'),
        ),
    ]
