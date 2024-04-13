# Generated by Django 5.0.2 on 2024-04-08 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='is_sold',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='available_colors',
        ),
        migrations.AddField(
            model_name='product',
            name='available_colors',
            field=models.ManyToManyField(blank=True, to='shop.color'),
        ),
    ]