from django.urls import path

from .views import index

app_name = 'payment'

urlpatterns = [
    path('', index, name='home'),
]
