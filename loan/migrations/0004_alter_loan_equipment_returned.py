# Generated by Django 4.2.3 on 2023-09-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0003_loan_all_returned_loan_equipment_returned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='equipment_returned',
            field=models.CharField(default='00:00', max_length=250),
        ),
    ]