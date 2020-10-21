from django.urls import path
from . import views
urlpatterns = [
    path('<int:prostu_id>/',views.detial,name='detials'),
    path('', views.hp, name='HomePage'),
]