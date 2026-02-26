from django.http import JsonResponse
from .models import Product

def product_list(request):
    data = list(Product.objects.values())
    return JsonResponse(data, safe=False)