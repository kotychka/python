from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addItem, name='add'),
    path('complete/<item_id>', views.completeItem, name='complete'),
    path('deleteCompleted', views.deleteCompleted, name='deleteCompleted'),
    path('delete', views.delete, name='delete'),


] 