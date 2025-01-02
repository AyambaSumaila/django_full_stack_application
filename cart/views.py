from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Item, Order
from movieapp.models import Movie
from .utils import calculate_cart_total
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    cart_total=0
    movies_in_cart=[]
    cart=request.session.get('cart', {})
    movie_ids=list(cart.keys())
    if(movie_ids != []):
        movies_in_cart=Movie.objects.filter(id__in=movie_ids)
        cart_total=calculate_cart_total(cart, movies_in_cart)
    template_data={} 
    template_data['title']='Cart'
    template_data['movies_in_cart']=movies_in_cart
    template_data['cart_total']=cart_total
    return render(request,'cart/index.html', {'template_data':template_data})   
 
def add_to_cart(request, id):
    
    get_object_or_404(Movie, id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('cart.index') 
 
 
def add(request, id):
    movie = get_object_or_404(Movie, id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('movieapp.show', id=id)
 
 
def clear(request):
     request.session['cart'] = {}
     return redirect('cart.index')
 

@login_required
def purchase(request):
    cart = request.session.get('cart', {})
    movie_ids=list(cart.keys())
    if(movie_ids == []):
        return redirect('cart.index')
    movies_in_cart=Movie.objects.filter(id__in=movie_ids)
    cart_total=calculate_cart_total(cart, movies_in_cart)
    order=Order()
    order.user=request.user
    order.total=cart_total
    order.save()
    for movie in movies_in_cart:
        item=Item()
        item.price=movie.price
        item.quantity=cart[str(movie.id)]
        item.order=order
        item.movie=movie
        item.save()
        
    request.session['cart'] = {}
    template_data={}
    template_data['title']='Purchase confirmation'    
    template_data['order_id'] = order.id
    return render(request,'cart/purchase.html', {'template_data':template_data})
      
 
 
 
 
 
 
 
 
 
 