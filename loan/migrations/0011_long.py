# Generated by Django 4.2.3 on 2023-10-03 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0010_alter_health_all_returned_alter_ref_all_returned'),
    ]

    operations = [
        migrations.CreateModel(
            name='Long',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('kit', models.CharField(max_length=150)),
                ('return_date', models.DateField(null=True)),
                ('returned', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.student')),
            ],
        ),
    ]