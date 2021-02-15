# Generated by Django 3.1.6 on 2021-02-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210210_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_code',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='ilosc',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='nazwa',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='opis',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='api.Product'),
        ),
    ]
