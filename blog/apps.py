from django.apps import \
    AppConfig  # Импортируем базовый класс для настройки приложения,AppConfig — это специальный класс,
# который помогает Django понять, как настроено приложение.


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'  # Указываем имя приложения (должно совпадать с именем папки приложения)
    verbose_name = "Блог"  # Указываем имя приложения (должно совпадать с именем папки приложения)
