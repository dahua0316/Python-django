# _*_ encoding:utf-8 _*_      # 用到了中文所以采用utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.contrib.auth.models import AbstractUser  # 继承django自带的类
from django.db import models


# Create your models here.


class UserProfile(AbstractUser):

    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default=' ')
    birday = models.DateField(verbose_name=u'生日', default=None, null=True, blank=True)
    gender = models.CharField(max_length=8, choices=(("male", u'男'), ("female", '女')), default="female")
    address = models.CharField(max_length=50, verbose_name=u'地址', default=' ')
    mobile = models.CharField(max_length=11, verbose_name=u'电话', null=True, blank=True, default=' ')
    image = models.ImageField(upload_to="image/%y/%m",  default=u"image/default.png", max_length=50)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmaildFyRond(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name="验证码类型", choices=(("register", u"注册"), ("forget", u"找回密码 ")), max_length=50)
    send_time = models.DateField(default=datetime.now, verbose_name=u"發送時間")

    class Meta:
        verbose_name = u"邮箱验证"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(max_length=100, upload_to="banner?/%Y/m", verbose_name=u"轮播图")
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=0, verbose_name=u"顺序 ")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name


