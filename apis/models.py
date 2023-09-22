from django.db import models

# Create your models here.

class Province(models.Model):
    pid = models.IntegerField(null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class District(models.Model):
    did = models.IntegerField(null=True)
    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class LocalGovernment(models.Model):
    lgid = models.IntegerField(null=True)
    province = models.ForeignKey(Province,on_delete=models.CASCADE,null=True)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=255)
    documents = models.ManyToManyField(Document)
    price = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    responsible_person = models.CharField(max_length=255)

    def __str__(self):
        return self.name