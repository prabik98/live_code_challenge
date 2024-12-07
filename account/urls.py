from django.urls import path
from rest_framework import routers
from account.views import SignupViewSet
from .views import image_request

account_router = routers.DefaultRouter()
account_router.register(r"account", SignupViewSet, basename="account")
urlpatterns = [  
    path('', image_request, name = "image-request")
]