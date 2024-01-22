# Generated by Django 4.2.8 on 2023-12-25 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SellingPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('wilaya', models.CharField(max_length=255)),
                ('moughataa', models.CharField(max_length=255)),
                ('commune', models.CharField(max_length=255)),
                ('gps_lat', models.FloatField()),
                ('gps_long', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ponderation', models.IntegerField()),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_21007.basket')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_21007.price')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('price_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('code', models.CharField(max_length=255)),
                ('productfamily', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_21007.productfamily')),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_21007.product'),
        ),
        migrations.AddField(
            model_name='price',
            name='sellingpoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_21007.sellingpoint'),
        ),
    ]
