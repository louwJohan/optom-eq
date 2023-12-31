# Generated by Django 4.2.3 on 2023-09-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_alter_loan_equipment_returned'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='date',
            field=models.DateField(auto_now_add=True, default='1988-12-12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loan',
            name='equipment_returned',
            field=models.CharField(default='None', max_length=250),
        ),
        migrations.AlterField(
            model_name='loan',
            name='time_returned',
            field=models.TimeField(default='12:00'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='time_taken',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
