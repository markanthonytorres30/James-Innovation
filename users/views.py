from django.shortcuts import render
from .models import Users

# Create your views here.
def index(request,user_code,user_pass):
    users_name = Users.objects.get(user_code=user_code)
    users_pass = Users.objetcs.get(user_password=user_pass)
