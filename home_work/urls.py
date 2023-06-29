from django.urls import path
from . import views

urlpatterns = [
    path('', views.doter),
    path('text/', views.text),
    path('page/', views.page),

]
