from django.shortcuts import render
from django.views.generic import View
from .models import City, CourseOrg
from .froms import UserAskform
from django.http import HttpResponse


# Create your views here.


class OrgView(View):
    """"
    课程机构列表首页
    """

    def get(self, request):
        # 查找所有城市
        all_city = City.objects.all()
        # 查找所有课程机构
        all_course = CourseOrg.objects.all()
        return render(request, 'org-list.html', {
            'all_city': all_city, 'all_course': all_course
        })

# 采用modelform进行


class UserAskView(View):
    def post(self, request):
        userask_form = UserAskform(request.POST)
        if userask_form.valid():
            userask = userask_form.save(commit=True)
            return HttpResponse("{'status':'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status':fail, msg:{0}}", format(userask_form.errors))
