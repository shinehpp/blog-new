from django.shortcuts import render, HttpResponse, redirect
from rbac.models import *
from luffy_permission import settings
import json


# Create your views here.


def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = UserInfo.objects.filter(name=username, password=password).first()
		if user:
			permission_queryset = user.roles.filter(permissions__isnull=False).values(
				"permissions__id",
				"permissions__title",
				"permissions__url",
				"permissions__name",
				"permissions__parent_id_id",
				"permissions__parent_id__title",
				"permissions__parent_id__url",
				"permissions__menu_id",
				"permissions__menu__title",
				"permissions__menu__icon"
			).distinct()
			menu_dict = {}
			permission_dict = {}
			for permission in permission_queryset:
				if not permission['permissions__menu_id']:
					permission_dict[permission["permissions__name"]] = {
						'title': permission['permissions__title'],
						'url': permission['permissions__url']
					}
					continue
				node = {'id': permission['permissions__id'], 'title': permission['permissions__title'],
							'url': permission['permissions__url']}
				menu_id = permission['permissions__menu_id']
				if menu_id in menu_dict:
					menu_dict[menu_id]['children'].append(node)
				else:
					menu_dict[menu_id] = {
						'title': permission['permissions__menu__title'],
						'icon': permission['permissions__menu__icon'],
						'children': [node, ]
					}
			request.session[settings.PERMISSION_M] = json.dumps(menu_dict)
			request.session[settings.PERMISSION_C] = json.dumps(permission_dict)
			return redirect('/customer/list/')
		else:
			return HttpResponse('error!')
