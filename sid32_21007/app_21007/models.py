from django.db import models

class ProductFamily(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label

class Product(models.Model):
    label = models.CharField(max_length=255)
    price_unit = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    productfamily = models.ForeignKey(ProductFamily, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

class SellingPoint(models.Model):
    code = models.CharField(max_length=255)
    wilaya = models.CharField(max_length=255)
    moughataa = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    gps_lat = models.FloatField()
    gps_long = models.FloatField()

    def __str__(self):
        return self.code

class Price(models.Model):
    value = models.DecimalField(max_digits=64, decimal_places=2)
    date = models.DateField()
    sellingpoint = models.ForeignKey(SellingPoint, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Basket(models.Model):
    label = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.label

class ProductBasket(models.Model):
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    ponderation = models.IntegerField()