# ！/uer/bin/ env python
# -*- utf-8 -*-
# author:dahua time:2018/10/5
import xadmin
from .models import City, CourseOrg, Teacher


class CityAdmin(object):
    pass
    # list_display = ["name ", "des ", " add_time"]
    # search_fields = ["name ", "des "]
    # list_filter = ["name ", "des ", " add_time"]


xadmin.site.register(City, CityAdmin)


class CourseOrgAdmin(object):
    pass
    # list_display = ["name ", "des ", " click_nums", " address", "city" ," add_time"]
    # search_fields = ["name ", "des ", " click_nums", " address", "city"]
    # list_filter = ["name ", "des ", " click_nums", " address", "city" ," add_time"]


xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):
    pass
    # list_display = ["org", " name  ", "work_years", " work_company", " points", " add_time"]
    # search_fields = ["org", " name  ", "work_years", " work_company", " points"]
    # list_filter = ["org", " name  ", "work_years", " work_company", " points"]


xadmin.site.register(Teacher, TeacherAdmin)

