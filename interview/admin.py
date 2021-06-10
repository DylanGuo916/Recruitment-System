from django.contrib import admin
from interview.models import Candidate
from datetime import datetime
# Register your models here.

# 候选人管理类
class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = ('username', 'city', 'bachelor_school', 'first_score', 'first_result', 'first_interviewer_user', 'second_score',
                    'second_result', 'second_interviewer_user', 'hr_score', 'hr_result', 'hr_interviewer_user',)

    ### 筛选条件
    list_filter = ('city', 'first_result', 'second_result', 'hr_result', 'first_interviewer_user', 'second_interviewer_user','hr_interviewer_user',)
    ### 查询字段
    search_fields = ('username', 'phone', 'email', 'bachelor_school',)
    ### 排序字段
    ordering = ('hr_result', 'second_result', 'first_result',)

    def save_model(self, request, obj, form, change):
        obj.last_editor = request.user.username
        if not obj.creator:
            obj.creator = request.user.username
        obj.modified_date = datetime.now()
        obj.save()

admin.site.register(Candidate, CandidateAdmin)
