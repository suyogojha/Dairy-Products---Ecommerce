from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.views import View
from .models import *
from django.db.models import Count


# Create your views here.
def home(request):
    return render(request, "app/home.html")

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).annotate(total=Count('title'))
        return render(request, "app/category.html", locals())