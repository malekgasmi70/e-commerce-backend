# Generated by Django 3.2.5 on 2021-07-15 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0004_commandeline_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acheteur', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.acheteur')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
