from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.template.defaultfilters import default
from django.forms.fields import ChoiceField
from django.db.models import Count
from django.db.models import Sum
# Create your models here.

class add_product(models.Model):
    product_Id = models.CharField(max_length=250,null=True,blank=True)
    Productname = models.TextField(null=True,blank=True)
    price = models.CharField(max_length=250,null=True,blank=True)
    stock = models.CharField(max_length=250,null=True,blank=True)
    imageurl = models.ImageField(upload_to="media/", null=True, blank=True,)
    category = models.CharField(max_length=250,null=True,blank=True)
    unit = models.CharField(max_length=250,null=True,blank=True)
    colour = models.CharField(max_length=250,null=True,blank=True)
    created_date = models.CharField(max_length=250,null=True,blank=True)
    created_by = models.CharField(max_length=250,null=True,blank=True)
    modified_date = models.DateTimeField(null=True,blank=True)
    modified_by = models.CharField(max_length=250,null=True,blank=True)


class add_cart(models.Model):
    product_Id = models.CharField(max_length=250,null=True,blank=True)
    quantity = models.CharField(max_length=250,null=True,blank=True)
    user = models.CharField(max_length=250,null=True,blank=True)
    created_date = models.DateTimeField(null=True,blank=True)
    created_by = models.CharField(max_length=250,null=True,blank=True)
    modified_date = models.DateTimeField(null=True,blank=True)
    modified_by = models.CharField(max_length=250,null=True,blank=True)
