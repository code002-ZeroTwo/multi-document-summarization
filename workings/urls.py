from django.urls import path

from . import views

urlpatterns = [
    path('', views.TitleView.as_view(), name='titles'),
    path('\summary', views.ContentView.as_view(), name='content'),
]