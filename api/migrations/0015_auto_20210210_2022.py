# Generated by Django 3.1.6 on 2021-02-10 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210210_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
