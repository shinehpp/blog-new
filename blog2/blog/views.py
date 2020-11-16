from django.shortcuts import render
from blog.utils.get_valid_image import get_image
from django.http import HttpResponse, JsonResponse
# Create your views here.


def login(request):
	if request.method == 'POST':
		print(1)
		response = {'user':None, 'msg':None}
		username = request.POST.get('username')
		password = request.POST.get('password')
		valid_code = request.POST.get('valid_code')
		code = request.session.get('code')
		if valid_code != code:
			response['msg'] = '验证码不正确！'
			return JsonResponse(response)
	return render(request,'login.html',locals())


def valid_code(request):
	data = get_image(request)
	return HttpResponse(data)
