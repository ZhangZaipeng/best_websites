#coding=utf-8
"""定义learning_logs的URL模式"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 登陆
    url(r'^login/$', views.login, name='login'),

    # 退出
    url(r'^loginout/$', views.loginout, name='loginout'),

    # 企业咨询
    url(r'^enterprise_new/$', views.enterprise_new, name='enterprise_new'),

    # 上传文件
    url(r'^file_upload/$', views.file_upload, name='file_upload'),
]

#错误页
handler404 = views.page404
handler500 = views.page500