from django.db import models

# Create your models here.


class Authority(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=32)


class Role(models.Model):
	id = models.AutoField(primary_key=True)
	role_name = models.CharField(max_length=32)
	authorities = models.ManyToManyField(to='Authority')


class UserInfo(models.Model):
	id = models.AutoField(primary_key=True)
	roles = models.ManyToManyField(to='Role')






