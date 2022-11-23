from django.urls import path
from app import views
from . import views


urlpatterns = [
    path("", views.home),
    path("about/", views.About, name="about"),
    path("contact/", views.Contact, name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
    path("product-details/<int:pk>", views.ProductDetails.as_view(), name="product-details"),
    
    
    #login authentication
]
