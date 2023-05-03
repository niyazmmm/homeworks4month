from django.shortcuts import render, redirect

from posts.forms import ProductCreateForm, CommentCreateForm
from posts.models import Product, Comment


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products,
            'user': request.user
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == "GET":
        form = CommentCreateForm()
        products = Product.objects.get(id=id)

        context = {
            'product': products,
            'comments': products.comment_set.all(),
            'form': form,
            'user': request.user
        }
        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                post_id=id
            )
            return redirect(f'/products/{id}/')

        context = {
            'product': product,
            'form': CommentCreateForm,
            'comment': product.comment_set.all()
        }
        return render(request, 'products/detail.html', context=context)


def product_create_view(request):
    if request.method == "GET":
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == "POST":
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
            )
            return redirect('/products/')
        return render(request, 'products/create.html', context={
            'form': form
        })
