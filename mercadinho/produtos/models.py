from django.db import models

class Produto(models.Model):
         
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default="")
    description = models.CharField(max_length=100, blank=False, default="")
    value = models.FloatField()
    id_category = models.ForeignKey('Categoria', related_name='produtos_idcategory_categorias', on_delete= models.PROTECT)
    category = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey('auth.User', related_name='produtos_owner_users', on_delete=models.PROTECT)

    def save(self, *args, **kwargs): 
        if self.value == 0:
            raise ValueError("O valor do produto não pode ser zero")
        if self.name == "":
            raise Exception("Produto sem nome")    
        if self.description == "":
            self.description = self.name
        self.category = {
            "id": self.id_category.id, 
            "name": self.id_category.name
            }
        super(Produto, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']

class Categoria(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default="")

    class Meta:
        ordering = ['created']