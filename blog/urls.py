from django.urls import path
from blog.views import (
    about_company_view, advices_view, delivery_payment_view, contacts_view,
    registration_view, login_view, logout_view
)

urlpatterns = [

    path('about_company/', about_company_view, name='about_company_url'),
    path('advices/', advices_view, name='advices_url'),
    path('delivery_payment/', delivery_payment_view, name='delivery_payment_url'),
    path('contacts/', contacts_view, name='contacts_url'),
    path('registration/', registration_view, name='registration_url'),
    path('login/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
]
