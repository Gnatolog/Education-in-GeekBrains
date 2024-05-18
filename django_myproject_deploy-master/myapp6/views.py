from django.shortcuts import render
from django.db.models import Sum

from myapp5.models import Product


def total_in_db(request):
    """Подсчет суммы в базе данных"""
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'The total number is calculated in the database',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_view(request):
    """Подсчет суммы в представление"""
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'The total number is calculated in the view function',
        'total': total,
    }

    return render(request,
                  'myapp6/total_count.html',
                  context)


def total_in_template(request):
    """Подсчет суммы в представление"""
    context = {
        'title': 'The total number is calculated in the template',
        'products': Product,
    }
    return render(request,
                  'myapp6/total_count.html',
                  context)
