# _*_ encoding:utf-8 _*_  # 用到了中文所以采用utf-8
from django.db import models
from datetime import datetime


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市")
    des = models.CharField(max_length=300, verbose_name=u"城市描述")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    des = models.TextField(verbose_name=u'机构描述')
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"封面图片")
    address = models.CharField(max_length=150, verbose_name=u"机构地址")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=u"所在城市")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,  on_delete=models.CASCADE, verbose_name=u"所在机构")
    name = models.CharField(max_length=50, verbose_name=u"教师姓名")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=150, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=150, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name
