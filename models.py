from django.db import models

# Create your models here.

class Server(models.Model):
	name = models.CharField(max_length=150)
	cmdbci = models.CharField(max_length=300)

class Process(models.Model):
	name = models.CharField(max_length=150)
	ads = models.CharField(max_length=300)
	port = models.IntegerField()
	url = models.CharField(max_length=300)
	server = models.ForeignKey(Server,on_delete=models.CASCADE)

class Service(models.Model):
	name = models.CharField(max_length=150)
	processes = models.ManyToManyField(Process)