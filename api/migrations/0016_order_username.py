# Generated by Django 3.1.6 on 2021-02-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20210210_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
