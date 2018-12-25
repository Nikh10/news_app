
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=256)
    parent_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class News(models.Model):
    news = models.CharField(max_length=512)
    description = models.TextField(max_length=512, null=True, blank=True)
    photos = models.TextField(default='https://images.unsplash.com/photo-1524821695732-717b25a38974?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=08f92fcbaca12ac3d128dbc91f447164&auto=format&fit=crop&w=1200&q=80')
    author = models.CharField(max_length=256)
    source = models.TextField(null=True, blank=True)
    posted_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.news