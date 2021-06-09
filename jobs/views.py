from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.detail import DetailView

from jobs.models import Job
from jobs.models import Cities, JobTypes
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User

from django.contrib.auth.decorators import permission_required, login_required
from django.views.decorators.csrf import csrf_exempt

import logging

def joblist(request):
    job_list = Job.objects.order_by('job_type')
    context =  {'job_list': job_list}
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JobTypes[job.job_type][1]
    return render(request, 'joblist.html', context)
