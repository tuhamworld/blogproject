from django.urls import path
from .views import index, create, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('update/<id>/', update, name='update'),
    path('delete/<id>/', delete, name='delete'),
]
