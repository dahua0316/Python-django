# ！/uer/bin/ env python
# -*- utf-8 -*-
# author:dahua time:2018/10/15
from django import forms
from operation.models import UserAsk


class UserAskform(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
