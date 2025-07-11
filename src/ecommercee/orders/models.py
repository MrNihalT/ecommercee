from django.db import models

from customers.models import Customer
from products.models import Product


class Order(models.Model):
    
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = (
        (ORDER_PROCESSED,"ORDER_PROCESSED"),
        (ORDER_DELIVERED,"ORDER_DELIVERED"),
        (ORDER_REJECTED,"ORDER_REJECTED"),     
    )
    order_status = models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    total_price = models.FloatField(default=0)
    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name="orders")
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Order-{}-{}".format(self.id,self.owner.user.username)

class OrderedItem(models.Model):
    product = models.ForeignKey(Product,related_name="added_carts",on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="added_items")
