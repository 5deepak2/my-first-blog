from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Company(models.Model):
    company_name=models.CharField(max_length=100)
    company_description=models.TextField(max_length=200)

class Category(models.Model):
    taxonomy=models.CharField(max_length=100)
    taxoterms=models.CharField(max_length=100)

class JobPost(models.Model):
    organisation=models.ForeignKey(Company)
    position=models.CharField(max_length=100)
    description=models.TextField()
    city=models.CharField(max_length=100)
    category=models.ForeignKey(Category,default='all')


    def __str__(self):
        return self.postion








