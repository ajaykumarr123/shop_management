# Generated by Django 2.2 on 2020-05-23 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_manager', '0004_auto_20200523_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='def_M.jpg', upload_to='product_img'),
        ),
    ]
