from django.contrib import admin
from .models import Item, OrderItem, Order
# Register your models here.

admin.site.regiter(Item)
admin.site.regiter(OrderItem)
admin.site.regiter(Order)
