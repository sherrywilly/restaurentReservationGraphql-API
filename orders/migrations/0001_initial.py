# Generated by Django 3.2.6 on 2021-08-07 09:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0002_alter_restaurant_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10)),
                ('guest', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('paymentmethod', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='BookingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.booking')),
            ],
        ),
    ]