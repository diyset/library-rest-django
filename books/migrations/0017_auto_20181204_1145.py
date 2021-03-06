# Generated by Django 2.1.3 on 2018-12-04 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20181204_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='code_borrow',
            field=models.CharField(blank=True, default='543A7A', max_length=8, null=True, unique=True),
        ),
    ]
