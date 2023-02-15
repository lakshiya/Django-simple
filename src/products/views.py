from django.shortcuts import render
from .models import Product
from .form import ProductForm
# Create your views here.

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = { 'obj' : obj}
    return render(request, 'product/product_detail.html', context)

def product_create_form(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    
    context = {'form': form}
    return render(request, 'product/product_create.html', context)
