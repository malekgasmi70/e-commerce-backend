# Generated by Django 3.2.5 on 2021-08-08 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210808_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.category'),
        ),
    ]
