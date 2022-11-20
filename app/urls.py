from django.urls import path
from . import views



urlpatterns = [
    path("", views.home),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
    path("product-details/<int:pk>", views.ProductDetails.as_view(), name="product-details"),
]
