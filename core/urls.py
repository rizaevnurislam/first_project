from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from shop.views import index_view

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('blog.urls')),
                  path('', include('shop.urls')),
                  path('cart/', include('shop_cart.urls')),
                  path("", index_view, name="index"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
