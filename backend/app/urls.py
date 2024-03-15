from django.urls import path

from . import views

urlpatterns = [
    path("sac/", views.SacView.as_view(), name="sac"),
    path("price/", views.PriceView.as_view(), name="price"),
    path("sacprice/", views.SacPriceView.as_view(), name="sacprice"),
]
