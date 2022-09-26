from django.urls import path

from .views import HomeIndexPage

urlpatterns = [
    path('', HomeIndexPage.as_view(), name='home'),
]