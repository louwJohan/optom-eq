# Generated by Django 4.2.3 on 2023-09-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0006_ref_health'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='recording_eq',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ref',
            name='recording_eq',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
