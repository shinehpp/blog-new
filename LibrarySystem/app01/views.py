from django.shortcuts import render, redirect
from app01.models import *
# Create your views here.


def index(request):
	book_list = Book.objects.all()
	author_list = Author.objects.all()
	publish_list = Publish.objects.all()

	return render(request, 'index.html', locals())


def add(request):
	if request.method == 'POST':
		publish = request.POST.get('publish')
		author = Author.objects.filter(id__in=request.POST.getlist("author"))
		book_obj = Book.objects.create(title=request.POST.get('title'), pub_date=request.POST.get('pub_date'), price=request.POST.get('price'), publish_id=publish)
		book_obj.authors.add(*author)
		return redirect('/app01/index/')
	publish_obj = Publish.objects.all()
	author_obj = Author.objects.all()
	return render(request, 'add.html', locals())


def delete(request, id):
	book_obj = Book.objects.get(id=id)
	book_obj.delete()
	return redirect('/app01/index/')


def update(request, id):
	book_obj = Book.objects.get(id=id)
	book_obj.pub_date = str(book_obj.pub_date)
	if request.method == 'POST':
		Book.objects.filter(id=id).update(title=request.POST.get('title'), pub_date=request.POST.get('pub_date'), price=request.POST.get('price'), publish=request.POST.get('publish'))
		return redirect('/app01/index/')
	return render(request, 'update.html',locals())