from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=100)
	#username = models.CharField(max_length=100)
	#email = models.CharField(max_length=200)
	#password = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name
	
class Badge(models.Model):
	name = models.CharField(max_length=200)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	presenter = models.CharField(max_length=200)
	#summary = models.CharField(max_length=1000)
	def __str__(self):
		return self.name