from django.shortcuts import render, get_object_or_404

from shop.models import Category
from shop_cart.models import Cart
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from shop.models import Favorite
from django.db.models import Q
from .models import Product
from .forms import ReviewForm


def index_view(request):
    categories = Category.objects.prefetch_related('children').filter(parent__isnull=True)
    products = Product.objects.all()[:4]  # Получаем 4 продукта для отображения
    cart = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'shop/index.html', {
        'categories': categories,
        'products': products,
        'cart': cart
    })


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()  # Получаем все товары этой категории
    return render(request, 'shop/category_detail.html', {'category': category, 'products': products})


from django.shortcuts import redirect


def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)

    if not created:
        favorite.delete()

    return redirect('shop:favorites')  # Перенаправление обратно на страницу избранного


@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('product')
    return render(request, 'shop/favorites.html', {'favorites': favorites})


def favorite_count_view(request):
    count = 0
    if request.user.is_authenticated:
        count = Favorite.objects.filter(user=request.user).count()
    return JsonResponse({"favorite_count": count})


def search_view(request):
    query = request.GET.get('q', '')  # Получаем параметр 'q' из GET-запроса
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'shop/search_results.html', {'query': query, 'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('shop:product_detail', product_id=product.id)

    return render(request, 'shop/product_detail.html', {'product': product, 'reviews': reviews, 'form': form})
