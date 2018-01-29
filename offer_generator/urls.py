from django.urls import path,re_path

from . import views

app_name = 'offer_generator'
urlpatterns = [
    path('', views.index, name='index'),
    path(r'item/', views.item, name='item'),
    path(r'item_group/', views.item_group, name='item_group')


    ]
