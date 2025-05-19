from shop.models import Category


def categories_context(request):
    categories = Category.objects.prefetch_related('children__children').filter(parent__isnull=True)
    return {'categories': categories}
