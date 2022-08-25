# Generated by Django 4.0.5 on 2022-08-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_favoritelist_favorite_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoritelist',
            name='favorite_product',
        ),
        migrations.AddField(
            model_name='favoritelist',
            name='favorite_product',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
