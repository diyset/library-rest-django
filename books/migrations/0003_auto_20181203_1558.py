# Generated by Django 2.1.3 on 2018-12-03 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20181203_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.BookCategory'),
        ),
    ]