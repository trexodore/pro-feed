from django.db import models

# Create your models here.
class Feed(models.Model):
    website = models.CharField(max_length=300,default="https://www.google.com")
    platform = models.CharField(max_length=35,default="woocommerce")
    pagination = models.IntegerField(default=0)
    brand_name = models.CharField(max_length=60,default="None")
    prod_condition = models.CharField(max_length=10,default="new")
    currency = models.CharField(max_length=5,default="USD")
    categories = models.BooleanField(default=False)
