# Generated by Django 2.1.3 on 2018-12-03 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20181203_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.BookCategory'),
        ),
        migrations.AlterField(
            model_name='bookcategory',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
