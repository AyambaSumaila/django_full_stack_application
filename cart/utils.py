def calculate_cart_total(cart, movie_in_cart):
    total = 0
    for movie in  movie_in_cart:
        quantity = cart[str(movie.id)]  # Get quantity from cart, default to 0 if not present.
        total += movie.price * int(quantity)
    return total