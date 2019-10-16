# Generated by Django 2.2.5 on 2019-10-15 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191015_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='blood_group',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=45, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_date_of_donation',
            field=models.DateField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='permanent_add',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='present_add',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
