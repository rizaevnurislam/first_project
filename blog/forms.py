from django import forms  # Импортируем модуль forms для работы с формами в Django
from django.contrib.auth.models import User  # Импортируем встроенную модель пользователя Django
from django.contrib.auth.forms import UserCreationForm, \
    AuthenticationForm  # Импортируем стандартные формы авторизации и регистрации


# Класс формы для авторизации пользователя (входа в систему)
class LoginForm(AuthenticationForm):
    # Поле для имени пользователя
    username = forms.CharField(
        label="Имя пользователя",  # Название поля в форме
        widget=forms.TextInput(attrs={  # Используем стандартное текстовое поле
            'class': 'form-control',  # Добавляем CSS-класс для стилизации Bootstrap
            'placeholder': 'Введите имя пользователя...'  # Подсказка внутри поля
        })
    )

    # Поле для ввода пароля
    password = forms.CharField(
        label="Пароль",  # Название поля
        widget=forms.PasswordInput(attrs={  # Поле типа "пароль" (скрывает вводимые символы)
            'class': 'form-control',  # CSS-класс для стилизации
            'placeholder': 'Введите пароль... '  # Подсказка внутри поля
        })
    )


# Класс формы для регистрации нового пользователя
class RegistrationForm(UserCreationForm):
    # Поле для имени пользователя (логина)
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя пользователя...'
        })
    )

    # Поле для имени (необязательное)
    first_name = forms.CharField(
        label="Ваше имя",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя...'
        })
    )

    # Поле для фамилии (необязательное)
    last_name = forms.CharField(
        label="Ваша фамилия",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Фамилия...'
        })
    )

    # Поле для электронной почты (обязательное)
    email = forms.EmailField(
        label="Ваш Email",
        widget=forms.EmailInput(attrs={  # Используем поле типа "email"
            'class': 'form-control',
            'placeholder': 'Email...'
        })
    )

    # Поле для ввода пароля (основной пароль)
    password1 = forms.CharField(
        label="Придумайте пароль",
        widget=forms.PasswordInput(attrs={  # Поле скрывает вводимые символы
            'class': 'form-control',
            'placeholder': 'Придумайте пароль... '
        })
    )

    # Поле для подтверждения пароля (проверка совпадения с password1)
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Подтвердите пароль... '
        })
    )

    # Вложенный класс Meta для настройки формы
    class Meta:
        model = User  # Указываем, что форма будет работать с моделью User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')  # Определяем, какие поля будут в форме
