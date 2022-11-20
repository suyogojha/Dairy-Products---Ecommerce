from django.urls import path
from . import views



urlpatterns = [
    path("", views.home),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
]
