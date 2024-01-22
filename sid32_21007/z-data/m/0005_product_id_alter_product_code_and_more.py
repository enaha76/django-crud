# Generated by Django 4.2.8 on 2024-01-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_21007', '0004_remove_product_id_alter_product_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sellingpoint',
            name='gps_lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sellingpoint',
            name='gps_long',
            field=models.FloatField(),
        ),
    ]