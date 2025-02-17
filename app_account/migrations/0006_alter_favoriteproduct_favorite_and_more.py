# Generated by Django 4.2.16 on 2024-10-10 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0007_alter_color_product'),
        ('app_account', '0005_alter_favoriteproduct_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteproduct',
            name='favorite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_products', to='app_account.favorite'),
        ),
        migrations.AlterField(
            model_name='favoriteproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_store.product'),
        ),
    ]
