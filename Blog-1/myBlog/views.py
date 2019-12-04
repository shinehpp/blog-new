from django.shortcuts import render, HttpResponse
from myBlog.myForms import *
from django.contrib import auth
from PIL import Image, ImageDraw, ImageFont
import random
import json
from io import BytesIO
from django.db.models import Count
from django.http import JsonResponse
from myBlog.models import *
from myBlog.geetest import GeetestLib



# Create your views here.

# 图片验证码登录起
pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"

def home(request):
	return render(request, "login2.html", )


def pcgetcaptcha(request):
	user_id = 'test'
	gt = GeetestLib(pc_geetest_id, pc_geetest_key)
	status = gt.pre_process(user_id)
	request.session[gt.GT_STATUS_SESSION_KEY] = status
	request.session["user_id"] = user_id
	response_str = gt.get_response_str()
	return HttpResponse(response_str)


def pcajax_validate(request):
	if request.method == "POST":
		gt = GeetestLib(pc_geetest_id, pc_geetest_key)
		challenge = request.POST.get(gt.FN_CHALLENGE, '')
		validate = request.POST.get(gt.FN_VALIDATE, '')
		seccode = request.POST.get(gt.FN_SECCODE, '')
		status = request.session[gt.GT_STATUS_SESSION_KEY]
		user_id = request.session["user_id"]
		if status:
			result = gt.success_validate(challenge, validate, seccode, user_id)
		else:
			result = gt.failback_validate(challenge, validate, seccode)
		res = {'user': None, 'msg': None}
		username = request.POST.get('username')
		pwd = request.POST.get('pwd')
		if request.session.get('img_text') == request.POST.get('code'):
			user = auth.authenticate(username=username, password=pwd)
			if user:
				auth.login(request, user)
				res['user'] = user.username
			else:
				res['msg'] = '用户名或密码不正确！'
		else:
			res['msg'] = '验证码不正确！'
		return HttpResponse(json.dumps(res))
	return HttpResponse("error")
# 图片验证码登录终


# 注册用户
def register(request):
	if request.method == 'POST':
		form1 = UserForm(request.POST)
		res = {'user': None, 'msg': None}
		if form1.is_valid():
			res['user'] = form1.cleaned_data.get('username')
			username = form1.cleaned_data.get('username')
			pwd = form1.cleaned_data.get('password')
			tel = form1.cleaned_data.get('telephone')
			email = form1.cleaned_data.get('email')
			avatar_obj = request.FILES.get('avatar')
			if avatar_obj:
				UserInfo.objects.create_user(username=username, password=pwd, telephone=tel, email=email, avatar=avatar_obj)
			else:
				UserInfo.objects.create_user(username=username, password=pwd, telephone=tel, email=email)
		else:
			res['msg'] = form1.errors
		return JsonResponse(res)

	form1 = UserForm()
	return render(request, 'register.html', locals())


# 数字验证码登录起
def login(request):
	if request.method == 'POST':
		res = {'user': None, 'msg': None}
		username = request.POST.get('username')
		pwd = request.POST.get('pwd')
		if request.session.get('img_text') == request.POST.get('code'):
			user = auth.authenticate(username=username, password=pwd)
			if user:
				auth.login(request, user)
				res['user'] = user.username
			else:
				res['msg'] = '用户名或密码不正确！'
		else:
			res['msg'] = '验证码不正确！'
		return JsonResponse(res)
	return render(request, "login.html", locals())


def code_pic(request):
	def random_color():
		col_num = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
		return col_num

	# 添加随机字符串和数字
	def random_text():
		random__num = str(random.randint(0, 9))
		random_lower = chr(random.randint(65, 90))
		random_upper = chr(random.randint(97, 122))
		text = random.choice([random__num, random_lower, random_upper])
		return text
	img = Image.new("RGB", (250, 32), color=random_color())  # 生成随机颜色的图片
	draw = ImageDraw.Draw(img)  # 获得画笔
	font_1 = ImageFont.truetype('/static/Gabriola.ttf', size=30)  # 文字字体和大小
	img_text = ''
	for i in range(6):
		t = random_text()
		draw.text((i*40+15, 0), t, random_color(), font=font_1)
		img_text = img_text + t
	request.session['img_text'] = img_text  # session传验证码键值
	print(img_text)
	# 加随机噪点
	width = 250
	height = 32
	for i in range(2):
		x1 = random.randint(0, width)
		x2 = random.randint(0, width)
		y1 = random.randint(0, height)
		y2 = random.randint(0, height)
		draw.line((x1, y1, x2, y2), fill=random_color())  # random_color() 随机颜色函数

	for i in range(10):
		draw.point([random.randint(0, width), random.randint(0, height)], fill=random_color())
		x = random.randint(0, width)
		y = random.randint(0, height)
		draw.arc((x, y, x + 4, y + 4), 0, 90, fill=random_color())

	# 将生成的图片存到内存里
	f = BytesIO()
	img.save(f, 'png')
	data = f.getvalue()  # 从内存里读取生成的图片数据
	return HttpResponse(data)
# 数字验证码登录终


#首页
def homepage(request):
	article_list = Article.objects.all()
	return render(request, 'index.html', locals())


# 个人站点
def home_site(request, username):
	username = username
	user_obj = UserInfo.objects.filter(username=username).first()
	my_blog = Blog.objects.filter(userinfo__username=username).first()
	print(my_blog)
	article_list = Article.objects.filter(user=user_obj)
	category_list = Category.objects.all()
	# tag_list = Tag.objects.filter(blog=my_blog)
	# 查询出tag及其对应的文章数
	tag_list = Tag.objects.filter(blog=my_blog).values("nid").annotate(c=Count("article__nid")).values_list("title", "c")
	# 查出category及其对应的文章数
	category_list = Category.objects.filter(blog=my_blog).values("nid").annotate(c=Count("article__nid")).values_list("title", "c")
	return render(request, 'site.html', locals())