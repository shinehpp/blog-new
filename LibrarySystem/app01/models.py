from django.db import models

# Create your models here.


class AuthorDetail(models.Model):
	id = models.AutoField(primary_key=True)
	birthday = models.DateField()
	telephone = models.CharField(max_length=11)
	address = models.CharField(max_length=50)


class Publish(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=10)
	city = models.CharField(max_length=10)
	email = models.CharField(max_length=20)


class Author(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=10)
	authorDetail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Book(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50)
	pub_date = models.DateField()
	price = models.DecimalField(max_digits=8, decimal_places=2)
	publish = models.ForeignKey(to="Publish", to_field="id", on_delete=models.CASCADE)
	authors = models.ManyToManyField(to="Author")

	def __str__(self):
		return self.title
