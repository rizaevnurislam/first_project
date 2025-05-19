from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from blog.forms import RegistrationForm, LoginForm


def index_view(request):
    return render(request, 'blog/index.html')


def about_company_view(request):
    return render(request, 'blog/about_company.html')


def advices_view(request):
    return render(request, 'blog/advices.html')


def delivery_payment_view(request):
    return render(request, 'blog/delivery_payment.html')


def contacts_view(request):
    return render(request, 'blog/contacts.html')


def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            context = {
                'title': 'Регистрация',
                'form': form,
                'errors': form.errors
            }
            return render(request, 'blog/registration.html', context)

    else:
        form = RegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'blog/registration.html', context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('index')
        else:
            context = {
                'title': 'Вход в аккаунт',
                'form': form,
                'errors': form.errors
            }
            return render(request, 'blog/login.html', context)

    else:
        form = LoginForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'blog/login.html', context)


def logout_view(request):
    logout(request)
    prev_page = request.META.get('HTTP_REFERER')
    return redirect(prev_page)

# from django.shortcuts import render
# from shop.models import Category, Product
#
#
# def index(request):
#     categories = Category.objects.all()
#     return render(request, 'index.html', {'categories': categories})
