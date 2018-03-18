from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from .models import Record
from django.template import loader
from django.http import Http404

# Create your views here.
def index(request):
     latest_product = Record.objects.order_by('-product')[:5]
     template = loader.get_template('sales/index.html')
     context = {
         'latest_product': latest_product,
     }
     return HttpResponse(template.render(context,request))

