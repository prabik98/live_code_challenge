from django.shortcuts import render

from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.forms import UserImage  
from account import serializers
from .models import UploadImage


class SignupViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = serializers.SignupSerializer


def image_request(request):  
    if request.method == 'POST':  
        form = UserImage(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImage()
  
    return render(request, 'image_form.html', {'form': form})  