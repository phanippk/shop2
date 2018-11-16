from django.contrib import admin

# Register your models here.
from app.models import *

class add_product_admin(admin.ModelAdmin):
    list_display =  ('product_Id','Productname','price','stock','imageurl','category','unit','colour','created_date','created_by','modified_date','modified_by')
admin.site.register(add_product,add_product_admin)

class add_cart_admin(admin.ModelAdmin):
    list_display =  ('product_Id','quantity','user','created_date','created_by','modified_date','modified_by')
admin.site.register(add_cart,add_cart_admin)