# Generated by Django 4.2.3 on 2023-09-13 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='equipment_taken',
            new_name='time_returned',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='equipment_returned',
        ),
        migrations.AddField(
            model_name='loan',
            name='room',
            field=models.CharField(default='0.00', max_length=10),
        ),
        migrations.AddField(
            model_name='loan',
            name='time_taken',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]