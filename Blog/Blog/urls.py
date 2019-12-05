"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from myBlog import views
from django.views.static import serve
from Blog import settings

urlpatterns = [
	path('admin/', admin.site.urls),
	path('reg/', views.register),
	path('index/', views.homepage),
	path('login/', views.login),
	# 点赞
	path('digg/', views.digg),
	path('comment/', views.comment_c),
	path('code_pic/', views.code_pic),
	# 文章详情页
	re_path('^(?P<username>\w+)/p/(?P<nid>.*)/$', views.article_info),
	# 个人站点页签
	re_path('^(?P<username>\w+)/(?P<key>tag|category|time)/(?P<value>.*)/$', views.home_site),
	# 个人站点
	re_path('^(?P<username>\w+)/$', views.home_site),
	# 使用图片验证登录起
	re_path(r'^pc-geetest/ajax_validate', views.pcajax_validate, name='pcajax_validate'),
	re_path(r'^pc-geetest/register', views.pcgetcaptcha, name='pcgetcaptcha'),
	re_path(r'^$', views.home, name='home'),
	# 使用图片验证登录终
	re_path(r"media/(?P<path>.*)", serve, {"document_root": settings.MEDIA_ROOT}),

]
