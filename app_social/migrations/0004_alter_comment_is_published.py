# Generated by Django 4.0.4 on 2024-09-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0003_alter_comment_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
