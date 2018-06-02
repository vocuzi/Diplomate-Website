from django.db import models
from django.utils import timezone
# Create your models here.
class Branch(models.Model):
    abbreviation=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=8)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.abbreviation

class Subject(models.Model):
    abbreviation=models.CharField(max_length=10,null=True)
    name=models.CharField(max_length=100)
    branch=models.ForeignKey('Branch',on_delete=models.CASCADE)
    semester=models.IntegerField()
    def __str__(self):
        return self.branch.abbreviation.upper()+" "+str(self.semester)+" - "+self.name

class File(models.Model):
    subject=models.ForeignKey('Subject',on_delete=models.CASCADE)
    year=models.IntegerField()
    hash=models.ForeignKey('UploadLogs',on_delete=models.CASCADE)
    def __str__(self):
        return self.subject.abbreviation+" "+str(self.year)

class UploadLogs(models.Model):
    useragent=models.CharField(max_length=200)
    ip_address=models.GenericIPAddressField()
    timestamp=models.DateTimeField(auto_now_add=True)
    filename=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    def __str__(self):
        return str(self.filename)+" ("+str(self.description[0:20])+")"


# class Paper(models.Model):
