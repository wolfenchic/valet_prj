from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from checkout.models import Order, OrderLineItem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def get_contact_page(request):
  return render(request, 'accounts/contact.html')
  
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("home")
    
def login(request):
    redirect_to = request.GET.get('next', 'home')
    
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            #Authenticate the user
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))
            
            # if the user is a user, and has correct password
            if user is not None:
                #Log them in
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect(redirect_to)
    
            else:
                # say no
                form.add_error(None, "Your username or password was not recognised")
        
    else:
        form = UserLoginForm()

    
    return render(request, 'accounts/login.html', { 'form': form })

@login_required()
def profile(request):
    orders = Order.objects.filter(user = request.user)
    order_detail = OrderLineItem.objects.all()
    return render(request, 'accounts/profile.html', {'orders': orders, 'order_detail': order_detail})
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('profile')

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form}) 