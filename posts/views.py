from django.shortcuts import render, redirect
from Shop4m.form import ProductCreateForm, CommentsCreateForm
from products.models import Products, Comment
from products.constanst import PAGINATION_LIMIT
from django.views.generic import ListView , CreateView, DetailView

# Create your views here.

class MainPageCBV(ListView):
    model = Products
    template_name ='layouts/index.html'

class ProductCBV(ListView , CreateView):
    model = Products
    template_name = 'products/products.html'
    context_object_name = 'products'

    def get(self , request , **kwargs):
        products = self.get_queryset()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        '''search'''
        if search:
            products = products.filter(title__icontains=search) | products.filter(description__icontains=search)
        '''pagination'''
        max_page = products.len() / PAGINATION_LIMIT
        max_page = round(max_page) + 1 if round(max_page) < max_page else round(max_page)

        '''product splice '''
        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]
        '''context'''
        context = {
            'products': products,
            "user": request.user,
            'pages': range(1, max_page + 1)
        }
        return render(request, 'products/products.html', context=context)



class ProductDetailCBV(DetailView, CreateView):
    model = Products
    template_name = 'products/detail.html'
    form_class = CommentsCreateForm
    pk_url_kwarg = 'id'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'product': self.get_object(),
            'Comments': Comment.objects.filter(product=self.get_object()),
            'form': kwargs.get('form', self.form_class)
        }

    def post(self, request, **kwargs):

        data = request.POST
        form = CommentsCreateForm(data=data)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                product_id=self.get_object().id
            )
            return redirect(f'/products/{self.get_object().id}/')

        return render(request, self.template_name, context=self.get_context_data(
            form=form
        ))
class CreateProductCBV(ListView, CreateView):
    model = Products
    template_name = 'products/create.html'
    form_class = ProductCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': self.form_class if not kwargs.get('form') else kwargs['form']
        }

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())

    def post(self, request, **kwargs):
        data, files = request.POST, request.FILES

        form = ProductCreateForm(data, files)

        if form.is_valid():
            Products.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price')
            )
            return redirect('/products/')

        return render(request, self.template_name, context=self.get_context_data(
            form=form
        ))
