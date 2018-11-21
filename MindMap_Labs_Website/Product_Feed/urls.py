from django.urls import path
from . import views

app_name = 'Product_Feed'

urlpatterns = [
    path('',views.prod_index,name='prod_index')
]
