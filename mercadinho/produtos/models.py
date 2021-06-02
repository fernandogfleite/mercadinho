from django.db import models
import json

class Product(models.Model):
         
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default="")
    description = models.CharField(max_length=100, blank=False, default="")
    price = models.FloatField()
    id_category = models.ForeignKey('Category', related_name='products_idcategory_categorys', on_delete= models.PROTECT)
    category = models.JSONField("Category")
    owner = models.ForeignKey('auth.User', related_name='products_owner_users', on_delete=models.PROTECT)

    def save(self, *args, **kwargs): 
        if self.price == 0:
            raise ValueError("O valor do produto não pode ser zero")
        if self.name == "":
            raise Exception("Produto sem nome")    
        if self.description == "":
            self.description = self.name
        self.category = {
            "id": self.id_category.id, 
            "name": self.id_category.name
            }
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']

class Category(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default="")

    class Meta:
        ordering = ['created']

class ShoppingCar(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, blank='False', default="teste")
    
    class Meta:
        ordering = ['data']

    @property
    def shoppingcar_totalprice(self):
        total = 0
        for product in self.products.all():
            total += product.total_price
        
        return total
class IndentifyShoppingCar(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    shoppingcar = models.ForeignKey('ShoppingCar', related_name="products", on_delete=models.PROTECT)
    product = models.ForeignKey('Product', related_name="product", on_delete=models.PROTECT)    
    quantity = models.PositiveIntegerField(blank=False, default=1)
    price = models.FloatField(blank=False, null=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price

        super(IndentifyShoppingCar,self).save(*args, **kwargs)
    class Meta:
        ordering = ['created']

    @property
    def total_price(self):
        return self.quantity * self.price