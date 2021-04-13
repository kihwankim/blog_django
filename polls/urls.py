from django.urls import path
from . import views

urlpatterns = [  # view 호출
    path('', views.index, name='index'),
]
