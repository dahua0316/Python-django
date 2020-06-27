# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login  # 用来认证
from django.contrib.auth.backends import ModelBackend  # 用来重新定义authenticate
from django.db.models import Q  # 使用交集
from .models import UserProfile
from .froms import LoginForm, RegisterFrom
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password


# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):
    def get(self, request):
        register_from = RegisterFrom()
        return render(request, "register.html", {"register_from": register_from})

    def post(self, request):
        register_from = RegisterFrom(request.POST)
        if register_from.is_valid():
            user_profile = UserProfile
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.save()
            pass


            pass


def Userlogin(resquest):
    if resquest.method == "POST":
        loginfrom = LoginForm(resquest.POST)
        if loginfrom.is_valid():
            user_name = resquest.POST.get("username", "")
            pass_word = resquest.POST.get("password", "")
            user = authenticate(username=user_name, passwoed=pass_word)
        if user is not None:
            login(resquest, user)
            return render(resquest, "index.html")
        else:
            return render(resquest, "login.html", {"msg": "输入错误"})
    elif resquest.method == "GET":
        return render(resquest, "login.html", {})
