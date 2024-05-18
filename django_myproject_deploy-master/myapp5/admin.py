from django.contrib import admin
from .models import Category, Product


@admin.action(description='Сбросить количество в ноль')
def reset_quantity(modeladmin, requset, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """
    List product
    """
    list_display = ['name', 'category', 'quantity']  # поля которые видим в админ панели
    ordering = ['category', '-quantity']  # сортировка
    list_filter = ['date_added', 'price']  # список для фильтрации
    search_fields = ['descripthion']  #  поле для поиска
    search_help_text = 'Поиск по полю Описания продукта (description)'  # подсказка для поиска а админ панели
    actions = [reset_quantity]  # подключение к админке действия

    """Отдельный продукт."""
    # fields = ['name','description','category','date_added','rating']
    readonly_fields = ['date_added', 'rating']  # поля только для чтения если
    # не добавить Django будет ругаться
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],  # скрыть поле
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован атоматически на основе отзывов покупателей',
                'fields': ['rating', 'date_added'],
            }
        )
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
