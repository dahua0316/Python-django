# ！/uer/bin/ env python
# _*_ encoding:utf-8 _*_
# author:dahua time:2018/10/5
from .models import Course, Lesson, Video, CourseResource
import xadmin


class CourseAdmin(object):
    list_display = ["name", "learn_time", "students", "fav_nums", "click_nums", "add_time"]
    search_fields = ["name", "learn_time", "students", "fav_nums", "click_nums"]
    list_filter = ["name", "learn_time", "students", "fav_nums", "click_nums", "add_time"]


xadmin.site.register(Course, CourseAdmin)


class LessonAdmin(object):
    list_display = ["course", "name", "add_time"]
    search_fields = ["course", "name"]
    list_filter = ["course__name", "name", "add_time"]


xadmin.site.register(Lesson, LessonAdmin)


class VideoAdmin(object):
    list_display = ["lesson", "name", "add_time"]
    search_fields = ["lesson", "name"]
    list_filter = ["lesson", "name", "add_time"]


xadmin.site.register(Video, VideoAdmin)


class CourseResourceAdmin(object):
    pass
    # list_display = ["course ", " name", "add_time"]
    # search_fields = [ "name"]
    # list_filter = ["course", "name", "add_time"]


xadmin.site.register(CourseResource, CourseResourceAdmin)
