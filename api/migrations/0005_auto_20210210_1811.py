# Generated by Django 3.1.6 on 2021-02-10 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210210_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='api.order'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_code',
            field=models.IntegerField(default=0),
        ),
    ]
