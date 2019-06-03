# Generated by Django 2.1.5 on 2019-05-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productforweek',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='productforweek',
            name='date',
            field=models.DateField(verbose_name='Date For'),
        ),
    ]