from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

#职位类型
JobTypes = [
    (0, "研发"),
    (1, "运营"),
    (2, "职能/支持"),
    (3, "产品"),
    (4, "设计"),
    (5, "市场"),
    (6, "教研教学"),
    (7, "销售"),
    (8, "游戏策划")
]

#职位城市
Cities = [
    (0, "北京"),
    (1, "上海"),
    (2, "深圳"),
    (3, "杭州"),
    (4, "成都"),
    (5, "广州"),
    (6, "武汉")
]

# 职位要求候选人学历
DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类别")
    job_name = models.CharField(max_length=250, blank=False, verbose_name="职位名称")
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name="工作地点")
    job_responsibility = models.TextField(max_length=1024, verbose_name="职位职责")
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="职位要求")
    creator = models.ForeignKey(User, verbose_name="创建人", null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)

    class Meta:
        verbose_name = '职位'
        verbose_name_plural = '职位列表'

    def __str__(self):
        return self.job_name

class Resume(models.Model):
    # 基本信息
    username = models.CharField(max_length=135, verbose_name='姓名')
    applicant = models.ForeignKey(User, verbose_name="申请人", null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=135, verbose_name='城市')
    phone = models.CharField(max_length=135,  verbose_name='手机号码')
    email = models.EmailField(max_length=135, blank=True, verbose_name='邮箱')
    apply_position = models.CharField(max_length=135, blank=True, verbose_name='应聘职位')
    born_address = models.CharField(max_length=135, blank=True, verbose_name='生源地')
    gender = models.CharField(max_length=135, blank=True, verbose_name='性别')

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name='本科学校')
    bachelor_major = models.CharField(max_length=135, blank=True, verbose_name='本科专业')
    master_school = models.CharField(max_length=135, blank=True, verbose_name='研究生学校')
    master_major = models.CharField(max_length=135, blank=True, verbose_name='研究生专业')
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name='博士生学校')
    doctor_major = models.CharField(max_length=135, blank=True, verbose_name='博士专业')
    major = models.CharField(max_length=135, blank=True, verbose_name='专业')
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name="学历")
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)

    # 候选人自我介绍，工作经历，项目经历
    candidate_introduction = models.TextField(max_length=1024, blank=True, verbose_name=u'自我介绍')
    work_experience = models.TextField(max_length=1024, blank=True, verbose_name=u'工作经历')
    project_experience = models.TextField(max_length=1024, blank=True, verbose_name=u'项目经历')

    class Meta:
        verbose_name = '简历'
        verbose_name_plural = '简历列表'

    def __str__(self):
        return self.username