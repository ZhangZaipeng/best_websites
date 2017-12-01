# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response,render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

from forms import LoginForm

import os
import uuid
import json

# Create your views here.
@login_required(login_url='login/')
def index(request):
    return render(request, 'admin_web/index.html')

# 登陆
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'admin_web/login.html', {'form': form,})
        # return render_to_response('admin_web/login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                request.session['username'] = username
                request.session.set_expiry(60*60*2)
                #return render_to_response('admin_web/index.html', RequestContext(request))
                return render(request,'admin_web/index.html')
            else:
                return render(request,'admin_web/login.html',{'form': form,'password_is_wrong':True})
        else:
            return render(request,'admin_web/login.html', {'form': form,})

# 退出
@login_required(login_url='login/')
def loginout(request):
    auth.logout(request)
    return HttpResponseRedirect("admin_web/login.html")

# 企业咨询
@login_required(login_url='login/')
def enterprise_new(request):
    return render(request, 'admin_web/enterprise_new.html')

# 文件上传
@csrf_exempt
def file_upload(request):
    ret = {'status': False, 'data': None, 'error': None}
    if request.method == 'POST':
        try:
            img = request.FILES.get('file')

            baseDir = os.path.dirname(os.path.abspath(__name__))
            id = uuid.uuid1()
            imgFullName = str(id) + str(img.name)
            fileDir = os.path.join(baseDir,'admin_web/static/images', imgFullName)
            f = open(fileDir, 'wb')

            for chunk in img.chunks(chunk_size=1024):
                f.write(chunk)

            ret['status'] = True
            ret['data'] = os.path.join('/static/images/',imgFullName)
        except Exception as e:
            ret['error'] = e
        finally:
            f.close()
            return HttpResponse(json.dumps(ret))
    return HttpResponse(json.dumps(ret))


######################################## 404 500 ##########################################

def page404(request):
    return render(request, '404.html')
def page500(request):
    return render(request, '500.html')

