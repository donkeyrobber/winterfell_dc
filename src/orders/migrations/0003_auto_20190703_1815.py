# Generated by Django 2.2.3 on 2019-07-03 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190703_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_items', to='orders.Order'),
        ),
    ]