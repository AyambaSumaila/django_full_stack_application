from django import template 
register =template.Library()


from django import template

register = template.Library()

@register.filter(name='get_quantity')
def get_cart_quantity(cart, movie_id):
    try:
        return cart[str(movie_id)]
    except KeyError:
        return 0




#@register.filter(name='get_quantity')
# def get_cart_quantity(cart, movie_id):
   # return cart[str(movie_id)]