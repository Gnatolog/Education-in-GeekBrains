from random import choice, randint, uniform

from django.core.management.base import BaseCommand
from myapp5.models import Category, Product


class Command(BaseCommand):
    help = " Generate fake products"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count quantity for generate')

    def handle(self, *args, **options):
        categories = Category.objects.all()
        products = []
        count = options.get('count')
        for i in range(1, count + 1):
            products.append(Product(
                name=f'продукт номер {i}',
                category=choice(categories),
                description='длинное описание продукта',
                price=uniform(0.01, 999_999.99),
                quantity=randint(1, 10_000),
                rating=uniform(0.01, 9.99),
            ))
        Product.objects.bulk_create(products)   #bulk_create добавляет все
                                                # содержимое списка в базу
                                                #данных одним запросом