#！/uer/bin/ env python
# -*- utf-8 -*-
# author:dahua time:2018/10/15
from django.urls import path, include
from .views import OrgView

urlpatterns = [
    path('list/', OrgView.as_view(), name="org_list"),
]