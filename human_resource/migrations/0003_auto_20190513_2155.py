# Generated by Django 2.1.5 on 2019-05-13 13:55

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0002_auto_20190513_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderforweek',
            name='test',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='supply', chained_model_field='products', horizontal=True, to='core.Product', verbose_name='TESTING'),
        ),
    ]
