from django.shortcuts import render, HttpResponse
from rbac.models import *

# Create your views here.


def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = UserInfo.objects.filter(name=username, password=password).first()
		if user:
			return HttpResponse('ok')
		else:
			return HttpResponse('error!')