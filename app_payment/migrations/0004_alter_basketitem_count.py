# Generated by Django 4.0.4 on 2024-10-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_payment', '0003_basket_date_created_basket_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
