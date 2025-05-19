class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def __iter__(self):
        """ Делаем корзину итерируемой, чтобы можно было использовать в шаблонах """
        for product_id, item in self.cart.items():
            yield {
                'product_id': product_id,
                'quantity': item['quantity'],
                'price': item['price'],
                'total_price': item['quantity'] * item['price']
            }

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity, 'price': float(product.price)}
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(item['quantity'] * item['price'] for item in self.cart.values())

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True
