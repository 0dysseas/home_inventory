# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 17:52
from __future__ import unicode_literals

from django.db import migrations

def create_dummy_products(apps, schema_editor):
    Product = apps.get_model('inventory', 'Product')

    Product(name='Biscuits', description='Papadopoulou Biscuits', price=2.52).save()
    Product(name='Rice', description='Agrino Rice', price=3.45).save()
    Product(name='Spaghetti', description='Barilla', price=2.10).save()
    Product(name='Canned Tomatoes', description='Kyknos', price=3.4).save()
    Product(name='Bacon', description='Nikas Bacon', price=2.85).save()
    Product(name='Croissants', description='Molto', price=3.5).save()
    Product(name='Beef', description='Ground', price=12.50).save()
    Product(name='Flour', description='Traditional Flour', price=3.50).save()
    Product(name='Oregano', description='Traditional oregano', price=0.70).save()


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_dummy_products),
    ]
