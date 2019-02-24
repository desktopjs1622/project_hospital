from django.urls import path
from apps.cuenta.views import index

from . import views

urlpatterns = [
    path('index/', 
        index.as_view(
            template_name = 'base_jinja.html',
        ), 
        name='vista-inicial'),
]