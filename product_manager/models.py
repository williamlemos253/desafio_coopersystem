from django.db import models
from django.utils.timezone import now
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    qtd = models.PositiveIntegerField()
    status = models.CharField(max_length=100, default='Disponível', blank=True, choices=[('Indisponível', 'Indisponível'), ('Disponível', 'Disponível')])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.qtd > 0:
            self.status = 'Disponível'
        else:
           self.status = 'Indisponível'
        super(Product, self).save(*args, **kwargs)



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qtd = models.IntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    request_date = models.DateTimeField(default=now, editable=False)
    requester = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    City = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Forwarding_agent = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=[('Pendente', 'Pendente'), ('Enviado', 'Enviado'), ('Entregue', 'Entregue')])


    def save(self, *args, **kwargs):
        if self.product.qtd < self.qtd:
            raise ValueError('Não existe estoque suficiente para o pedido') 
        else:
            self.unit_price = self.product.price
            self.total_price = self.unit_price * self.qtd
            self.product.qtd -= self.qtd
            self.product.save()
        super(Order, self).save(*args, **kwargs)
