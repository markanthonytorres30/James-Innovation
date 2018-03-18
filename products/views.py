from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.template import loader
from django.http import Http404

def index(request):
    latest_product = Product.objects.order_by('-product_imei')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_product': latest_product,
    }
    
    return HttpResponse(template.render(context,request))

def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'detail.html', {'product': product})

def results(request, product_id):
    response = "Products is %s."
    return HttpResponse(response % product_id)
