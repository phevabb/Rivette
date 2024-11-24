from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('pay/<uuid:token_number>/', views.payment, name='payment'),


]