from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return self.name

class ItemGroup(models.Model):
    name = models.CharField(max_length=30)

    sub_groups = models.ManyToManyField("self",blank = True)
    sub_items = models.ManyToManyField(Item,blank = True)

    def __str__(self):
        return self.name

    @property
    def price(self):

        price = 0
        for sub_item in self.sub_items.all():
            price+=sub_item.price

        for sub_group in self.sub_groups.all():
            price += sub_group.price

        return price

class Offer(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    sub_items = models.ManyToManyField(Item, blank=True)
    sub_item_groups = models.ManyToManyField(ItemGroup, blank=True)

    def __str__(self):
        return self.name

    @property
    def price(self):

        price = 0
        for sub_item in self.sub_items.all():
            price+=sub_item.price

        for sub_group in self.sub_item_groups.all():
            price += sub_group.price

        return price