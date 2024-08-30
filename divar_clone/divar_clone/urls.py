from django.urls import path
from . import views

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('create/', views.ad_create, name='ad_create'),
    path('<int:ad_id>/delete/', views.ad_delete, name='ad_delete'),
]

