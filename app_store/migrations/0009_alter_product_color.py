# Generated by Django 4.2.16 on 2024-10-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0008_rename_color_name_color_name_remove_color_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, to='app_store.color'),
        ),
    ]
