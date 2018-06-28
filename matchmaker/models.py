from django.db import models
from djchoices import ChoiceItem, DjangoChoices


class OrderSide(DjangoChoices):
    buy = ChoiceItem(1)
    sell = ChoiceItem(2)


class Instrument(models.Model):

    label = models.CharField(max_length=10)
    """ The simple trading label for this instrument """

    name = models.CharField(max_length=32)
    """ A more descriptive name for the instrument """

    def __str__(self):
        return "%s (%s)" % (self.label, self.name)


class OrderBook(models.Model):

    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    """ What instrument is being traded """

    def __str__(self):
        return "Order book for %s" % self.instrument


class Order(models.Model):
    """
    Represents a single purchase order
    """

    placed_at = models.DateTimeField(auto_now_add=True)
    """ When the order was placed """

    book = models.ForeignKey(OrderBook, on_delete=models.CASCADE)
    """ Which order book this order belongs to """

    side = models.SmallIntegerField(choices=OrderSide.choices)
    """ Whether the order is a bid(buy) or an ask(sell) """

    price = models.DecimalField(max_digits=10, decimal_places=5)
    """ The price the order is placed at """

    total_quantity = models.DecimalField(max_digits=10, decimal_places=5)
    """ The total amount of the instrument requested for buy/sell """

    filled_quantity = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    """ How much of the order has been filled so far """
