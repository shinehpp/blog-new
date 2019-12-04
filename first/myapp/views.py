from django.shortcuts import render, HttpResponse

# Create your views here.


def timer(request):
    import time
    c_time = time.time()
    return render(request, 'index.html', {'date': c_time})


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('psd')
        if name == 's' and password == '123':
            return HttpResponse('登录成功！')
        else:
            return HttpResponse('用户名或密码错误！')
    else:
        return render(request,'login.html')