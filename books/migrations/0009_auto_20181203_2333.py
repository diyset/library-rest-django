# Generated by Django 2.1.3 on 2018-12-03 16:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_order_code_borrow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code_borrow',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True, unique=True),
        ),
    ]
