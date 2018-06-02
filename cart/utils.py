from django.shortcuts import get_object_or_404
from services.models import Service
from decimal import Decimal

def get_cart_items_and_total(cart):
    cart_items = []
    total = 0
    for item_id, item_quantity in cart.items():
        this_service = get_object_or_404(Service, pk=item_id)
        this_total = this_service.price * Decimal(item_quantity)
        total += this_total
        this_item = {
            'service_id': item_id, 
            'name': this_service.name,
            'quantity': item_quantity,
            'price': this_service.price,
            'total': this_total,
        }
        cart_items.append(this_item)

    return { 'cart_items': cart_items, 'total': total }