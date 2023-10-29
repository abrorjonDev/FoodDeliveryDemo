# Generated by Django 3.2.9 on 2023-10-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_rename_food_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('delivered', 'Delivered')], default='pending', max_length=10),
        ),
    ]