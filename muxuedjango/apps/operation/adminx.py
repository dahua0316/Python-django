# ！/uer/bin/ env python
# -*- utf-8 -*-
# author:dahua time:2018/10/5
import xadmin
from .models import UserAsk, CourseComments, UserMessage, UserCourse, UerFavorite


class UserAskAdmin(object):
    list_display = ["name", "mobile", "course_name", "add_time"]
    search_fields = ["name", "mobile", "course_name"]
    list_filter = ["name", "mobile", "course_name", "add_time"]


xadmin.site.register(UserAsk, UserAskAdmin)


class CourseCommentsAdmin(object):
    pass
    # list_display = ["user", "comment ", "add_time"]
    # search_fields = ["user", "comment "]
    # list_filter = ["user", "comment ", "add_time"]


xadmin.site.register(CourseComments, CourseCommentsAdmin)


class UerFavoriteAdmin(object):
    pass
    # list_display = ["user", "fav_id",  "add_time"]
    # search_fields = ["user", "fav_id"]
    # list_filter = ["user", "fav_id",  "add_time"]


xadmin.site.register(UerFavorite, UerFavoriteAdmin)


class UserMessageAdmin(object):
    pass
    # list_display = ["user", "message", " has_read", "add_time"]
    # search_fields = ["user",  "message", " has_read"]
    # list_filter = ["user",  " has_read", "add_time"]


xadmin.site.register(UserMessage, UerFavoriteAdmin)


class UserCourseAdmin(object):
    list_display = ["user", "course", "add_time"]
    search_fields = ["user", "course"]
    list_filter = ["user", "course", "add_time"]


xadmin.site.register(UserCourse,UserCourseAdmin )

