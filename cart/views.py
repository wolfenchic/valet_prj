from django.shortcuts import render, redirect, get_object_or_404
from services.models import Service
from decimal import Decimal
from cart.utils import get_cart_items_and_total

def view_cart(request):
    cart = request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    return render(request, "cart/view_cart.html", context)
 

def add_to_cart(request):
    id = request.POST['id']
    quantity = int(request.POST['quantity'])

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    
    request.session['cart'] = cart   

    return redirect('home')



def delete_cart_item(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart   
    return redirect('view_cart')    
# Create your views here.
