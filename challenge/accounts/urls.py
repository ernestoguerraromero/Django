from django.urls import path, include

from . import views
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()

router.register(r'accounts', views.AccountViewSet)

urlpatterns = [
    path('fizz-buzz/', views.fizz_buzz),
    path('',include(router.urls))
]

