# Generated by Django 2.1.5 on 2019-03-03 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='supplier_id',
        ),
    ]