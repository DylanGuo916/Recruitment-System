from django.conf.urls import url
from jobs import views
from django.urls import path

urlpatterns = [
    # 职位列表
    path("joblist/", views.joblist, name="joblist"),
    # 职位详情
    path('job/<int:job_id>/', views.detail, name='detail'),
    #默认显示页面
    url(r"$", views.joblist, name="name"),
]