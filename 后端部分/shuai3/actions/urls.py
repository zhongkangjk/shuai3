from django.urls import path
from . import views

app_name = 'actions'

urlpatterns = [	
    path('test/', views.test, name='test'),

]