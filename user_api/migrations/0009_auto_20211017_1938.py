# Generated by Django 3.2.8 on 2021-10-17 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0008_auto_20211017_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.IntegerField(null=True),
        ),
    ]
