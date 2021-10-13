# Generated by Django 3.2.8 on 2021-10-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0004_auto_20211011_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='zipcode',
            field=models.IntegerField(null=True),
        ),
    ]