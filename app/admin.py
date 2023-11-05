from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced
)

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','Name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','brand','category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quentity']

@admin.register(OrderPlaced)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','customer','quentity','ordered_date','status']
