# Generated by Django 5.1.1 on 2024-09-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_main', '0003_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=2),
        ),
    ]
