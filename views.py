from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from mynav.mycoach_nav import main_nav, tasks_nav
from .models import *
#from .forms import *
from django.conf import settings


# Create your views here.


def test_view(request):
    return HttpResponse('testing page')

#@staff_member_required
def home_view(request):
    return render(request, settings.MYDATA+'/home.html', {
        "main_nav": main_nav(request.user, 'student_view'),
        #"tasks_nav": tasks_nav(request.user, 'publisher'),
        #"steps_nav": steps_nav(request.user, 'run_checkout')
    })


