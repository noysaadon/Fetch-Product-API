# Generated by Django 4.0.5 on 2022-08-22 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='email',
        ),
    ]
