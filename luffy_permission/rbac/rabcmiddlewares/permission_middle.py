from django.utils.deprecation import MiddlewareMixin


class MyPermissionMiddleware(MiddlewareMixin):

	def process_request(self, request):
		pass