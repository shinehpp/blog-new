from django.utils.deprecation import MiddlewareMixin
from luffy_permission import settings
import json
import re


class MyPermissionMiddleware(MiddlewareMixin):

	def process_request(self, request):
		# m_dict = json.loads(request.session.get(settings.PERMISSION_M))
		# c_dict = json.loads(request.session.get(settings.PERMISSION_C))
		# print(m_dict)
		# print(c_dict)
		# print(request.path)
		pass
