from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return self.name

class ItemGroup(models.Model):
    name = models.CharField(max_length=30)

    sub_groups = models.ManyToManyField("self")
    sub_items = models.ManyToManyField(Item)

    def __str__(self):
        return self.name


