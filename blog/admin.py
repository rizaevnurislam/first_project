from django.contrib import admin  # Импортируем модуль админки Django

from blog.models import *  # Импортируем все модели из приложения blog

admin.site.register(Post)  # Регистрируем модель Post, чтобы она отображалась в админке Django
