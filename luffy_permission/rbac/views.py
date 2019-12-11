from django.shortcuts import render, HttpResponse
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
			m_list = Permission.objects.filter(role__id=user.id)
			m_dict = {}
			c_dict = {}
			for m in m_list:
				value = {
					'title': m.title,
					'url': m.url,
					'is_menu': m.is_menu,
				}
				if not m.parent_id_id:
					m_dict[m.id] = value
				else:
					value['pid'] = m.parent_id.id
					c_dict[m.id] = value
			request.session[settings.PERMISSION_M] = json.dumps(m_dict)
			request.session[settings.PERMISSION_C] = json.dumps(c_dict)
			return HttpResponse('ok')
		else:
			return HttpResponse('error!')