# Generated by Django 4.0.4 on 2022-05-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workmodel',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
    ]