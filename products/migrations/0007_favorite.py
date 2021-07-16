# Generated by Django 3.2.5 on 2021-07-15 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0006_auto_20210715_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acheteur', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.acheteur')),
                ('product', models.ManyToManyField(null=True, to='products.Product')),
            ],
        ),
    ]
