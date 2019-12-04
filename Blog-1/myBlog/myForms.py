from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from myBlog.models import *


class UserForm(forms.Form):
	username = forms.CharField(min_length=4, label='姓名', widget=widgets.TextInput(attrs={'class': 'form-control'}), error_messages={"required": "用户名不能为空！"})
	password = forms.CharField(min_length=6, label='密码', widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
	ret_password = forms.CharField(min_length=6, label='确认密码', widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
	telephone = forms.CharField(min_length=11, label='电话号码', widget=widgets.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='邮箱', widget=widgets.EmailInput(attrs={'class': 'form-control'}))

	def clean_username(self):
		name = self.cleaned_data.get('username')
		ret = UserInfo.objects.filter(username=name)
		if ret:
			raise ValidationError('用户名已存在！')
		else:
			return name

	def clean(self):
		pwd = self.cleaned_data.get('password')
		re_pwd = self.cleaned_data.get('ret_password')
		if pwd and re_pwd and pwd != re_pwd:
			raise ValidationError('两次输入的密码不一致！')
		else:
			return self.cleaned_data
