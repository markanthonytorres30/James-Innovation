# Generated by Django 2.0.3 on 2018-03-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='inventory_order',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='inventory_quantity',
            field=models.IntegerField(default=1),
        ),
    ]
