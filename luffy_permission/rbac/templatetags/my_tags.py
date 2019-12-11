from django import template
import json
from luffy_permission import settings
import re


register = template.Library()


@register.inclusion_tag('menu.html')
def menu_tag(request):
	m_dict = json.loads(request.session.get(settings.PERMISSION_M))
	return {'m':m_dict}


@register.filter()
def get_value(request, t_url):
	c_dict = json.loads(request.session.get(settings.PERMISSION_C))
	print('----------------')
	for key, value in c_dict.items():
		p_url = '^'+value['url']+'$'
		print(re.match(p_url, t_url))
		if re.match(p_url, t_url):
			return True
	else:
		return False
