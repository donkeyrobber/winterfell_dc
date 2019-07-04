from django.db import models


class Item(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):

    VAT_MULTIPLIER = 1.2

    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def summarise(self):

        total = 0
        for item in self.line_items.all():
            total += item.price * item.quantity

        total = float(total)
        net = round(total / Order.VAT_MULTIPLIER, 2)
        vat = round(total - net, 2)

        totals = {
            'total': total,
            'net': net,
            'vat': vat,
            }
        return totals


class LineItem(models.Model):

    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='line_items'
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(
        models.constraints.CheckConstraint(
            check=models.Q(quantity__gt=0), name='quantity_gt0')
    )

    class Meta:
        unique_together = ('order', 'item')

    def total(self):
        return self.price * self.quantity
