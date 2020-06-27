# ！/uer/bin/ env python
# -*- utf-8 -*-
# author:dahua time:2018/10/4
import xadmin
from xadmin import views
from .models import EmaildFyRond, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "慕雪台管理系统"
    site_footer = "慕雪大脸教育网"
    menu_style = "accordion"







class EmailFyRecordAdmin(object):
    list_display = ["code", "email", "send_type", "send_time"]
    search_fields = ["code", "email", "send_type"]
    list_filter = ["code", "email", "send_type", "send_time"]


xadmin.site.register(EmaildFyRond, EmailFyRecordAdmin)


class BannerAdmin(object):
    list_display = ["title", "image", "url", "index", "add_time"]
    search_fields = ["title", "image", "url", "index", ]
    list_filter = ["title", "image", "url", "index", "add_time"]


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

