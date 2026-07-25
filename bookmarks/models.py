from django.db import models
from django.contrib.auth.models import User

class Collection(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE,blank=False)
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name

class Tag(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE,blank=False)
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name

class Bookmark(models.Model):
    VISIBILITY_CHOICES=[
        ("public","Public"),
        ("private","Private"),
    ]
    owner=models.ForeignKey(User, on_delete=models.CASCADE,blank=False)
    title=models.CharField(blank=False)
    url=models.URLField(unique=False)
    description=models.TextField(blank=True)
    visibility=models.CharField(max_length=100,choices=VISIBILITY_CHOICES)
    tags=models.ManyToManyField(Tag,blank=True)
    collections=models.ManyToManyField(Collection,blank=True)
    created_at=models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)