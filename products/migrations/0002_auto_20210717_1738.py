# Generated by Django 3.2.5 on 2021-07-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(null=True, to='products.ProdImage'),
        ),
    ]
