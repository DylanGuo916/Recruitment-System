from django.conf.urls import url
from jobs import views
from django.urls import path

urlpatterns = {
    # 职位列表
    path("joblist/", views.joblist, name="joblist"),
}