# Generated by Django 4.2.6 on 2023-11-25 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_avalable',
            field=models.BooleanField(default=False),
        ),
    ]
