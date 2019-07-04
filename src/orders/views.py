from django.template.response import SimpleTemplateResponse
from django.db.models import Sum, DecimalField, F
from .models import Order


def index(request):
    order_id = request.GET.get('order_id', '')
    context = {'order_id': order_id}

    if order_id:
        try:
            order = Order.objects.get(id=order_id)
            context['order_details'] = order
            context['line_items'] = order.line_items.annotate(
                total=Sum(F('price') * F('quantity'),
                          output_field=DecimalField(decimal_places=2)
                          )
            ).values(
                'id',
                'order_id',
                'item__name',
                'price',
                'quantity',
                'total',
            )
            context['vat_breakdown'] = order.summarise()
        except Order.DoesNotExist:
            context['message'] = "Order does not exist"
    else:
        context['message'] = "Please search for an order"

    return SimpleTemplateResponse('index.html', context)
