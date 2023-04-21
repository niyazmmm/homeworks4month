from django.shortcuts import render
from posts.models import Product


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == "GET":
        products = Product.objects.get(id=id)

        context = {
            'product': products,
            'comments': products.comment_set.all()
        }
        return render(request, 'products/detail.html', context=context)
