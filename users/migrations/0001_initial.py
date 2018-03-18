# Generated by Django 2.0.3 on 2018-03-18 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0002_auto_20180318_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privelege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privelege_code', models.CharField(max_length=5)),
                ('privelege_name', models.CharField(max_length=10)),
                ('privelege_description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_code', models.CharField(max_length=10)),
                ('user_name', models.CharField(max_length=50)),
                ('user_phone', models.IntegerField(default=123456789)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=10)),
                ('user_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Location')),
                ('user_privelege', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Privelege')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType_code', models.IntegerField(default=1)),
                ('userType_name', models.CharField(max_length=10)),
                ('userType_description', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserType'),
        ),
    ]