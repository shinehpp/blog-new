from django import template
from django.db.models import Count
from django.db.models.functions import *
from myBlog import models

register = template.Library()


@register.inclusion_tag("class_tag.html")
def get_classification_style(username):
	article_list = models.Article.objects.filter(user__username=username)
	user = models.UserInfo.objects.filter(username=username).first()
	my_blog = user.blog
	category_list = models.Category.objects.filter(blog=my_blog).values("nid").annotate(c=Count("article__nid")).values_list("title", "c")
	tag_list = models.Tag.objects.filter(blog=my_blog).values("nid").annotate(c=Count("article__nid")).values_list("title", "c")
	time_list = article_list.annotate(month=TruncMonth("create_time")).values("month").annotate(c=Count("nid")).values_list("month", "c")
	return {"blog": my_blog, "category_list":category_list, "tag_list": tag_list, "time_list":time_list, "username": username}