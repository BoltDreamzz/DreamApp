# Generated by Django 5.0.2 on 2024-04-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_color_product_is_sold_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=10),
        ),
    ]
