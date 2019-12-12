from django import template
import json
from luffy_permission import settings


register = template.Library()


@register.inclusion_tag('menu.html')
def menu_tag(request):
	m_dict = json.loads(request.session.get(settings.PERMISSION_M))
	return {'m': m_dict}


@register.filter()
def get_value(request, name):
	m = request.session.get(settings.PERMISSION_M)
	c = request.session.get(settings.PERMISSION_C)
	if name in m or name in c:
		return True
