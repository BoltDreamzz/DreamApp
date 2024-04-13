from .cart import Cart


# Use context processor to manage our sessions

def cart(request):
    # return the default data from cart
    return {"cart": Cart(request)}
