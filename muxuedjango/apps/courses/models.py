# _*_ encoding:utf-8 _*_  # 用到了中文所以采用utf-8
from django.db import models
from datetime import datetime


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    des = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.CharField(max_length=300, verbose_name=u"课程描述")
    degree = models.CharField(max_length=10, choices=(("cj", u"初级"), ("zj", u"中级"), ("gj", u"高级")), default=u"cj")
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="course/%Y/m", verbose_name=u"封面")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=u"章节")
    name = models.CharField(max_length=20, verbose_name=u"视频")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"下载")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
