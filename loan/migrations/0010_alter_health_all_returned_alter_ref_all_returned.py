# Generated by Django 4.2.3 on 2023-09-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0009_alter_health_stand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='all_returned',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='ref',
            name='all_returned',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
