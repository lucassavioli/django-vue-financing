from django.urls import path
from . import views

urlpatterns = [
    path("sac/", views.SacView.as_view()),
    path("price/", views.PriceView.as_view()),
]
