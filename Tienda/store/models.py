from django.db import models

class gafas(models.Model):
    Id=models.IntegerField
    ItemName=models.TextField(max_length=255)
    ItemCategory=models.TextField(max_length=255)
    Price=models.IntegerField
    Price=models.IntegerField
    

class Bodega(models.Model):
    ItemId=models.ForeignKey(Product,on_delete=models.CASCADE)
    BodegaID=models.IntegerField
    location=models.TextField(max_length=100)
    ItemStock=models.IntegerField