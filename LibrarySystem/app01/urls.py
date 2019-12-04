from django.urls import re_path, path
from app01 import views

urlpatterns = [
	re_path('index/', views.index),
	re_path('add/', views.add),
	path('delete/<int:id>', views.delete),
	path('update/<int:id>', views.update),
]
