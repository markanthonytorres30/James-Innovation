# Generated by Django 2.0.3 on 2018-03-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_num', models.IntegerField(default=1)),
                ('category_name', models.CharField(max_length=100)),
                ('category_description', models.CharField(max_length=500)),
            ],
        ),
    ]
