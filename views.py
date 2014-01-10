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

@staff_member_required
def Download_Mysql_View(request):
    import pdb; pdb.set_trace() 
    import os, time
    # if not admin don't do it
    staffmember = request.user.is_staff
    if not staffmember:
        return redirect('/')

    # send the results
    try:
        now = time.strftime('%Y-%m-%d-%H-%M-%S')         
        file_name = settings.DB_NAME + "_" + now + ".sql"
        file_path = settings.DIR_DOWNLOAD_DATA + "mysql/" + file_name
        
        os.system("mysqldump -u ecoach -pecoach " + settings.DB_NAME + " > " + file_path)

        fsock = open(file_path,"rb")
        response = HttpResponse(fsock, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=' + file_name            
    except IOError:
        response = HttpResponseNotFound("error creating backup database file")

    return response


