class Cart():
    def __init__(self, request):
        self.session = request.session

        # get current session key if available

        cart = self.session.get("session_key")

        # if the user is new, no session exists, create one
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # to ensure that we have the cart on all pages
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {"price": str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)  # This returns the qty of items in cart
