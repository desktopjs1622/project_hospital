from django.urls import path
from apps.cuenta.views import index

from . import views

urlpatterns = [
    path('inicio/', views.index, name='index'),
    path('inicio2/', 
        index.as_view(
            template_name = 'base_jinja.html',
        ), 
        name='index2'),
]