# encoding:utf-8

from __future__ import unicode_literals
from simditor.fields import RichTextField
from django.db import models
import re

class Articles(models.Model):
    titlePage = models.ImageField(upload_to='live/',blank=True,null=True)
    title = models.TextField( blank=True, null=True)
    keyword = models.CharField(max_length=100, blank=True, null=True)
    content = RichTextField()
    name = models.CharField(max_length=50, blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # 展示HTML文本
    def get_desc(self):
        html = self.content
        dr = re.compile(r'<[^>]+>', re.S)
        dd = dr.sub('', html)
        if(len(dd) > 300):
            return dd[0:300] + "..."
        return dd + "..."

    def get_eng_month(self):
        month = ['January','February','March','April','May','June','July','Aguest','September','October','November','December']
        return month[int(self.created_at.month()) - 1]

    def get_likes(self):
        if(self.like == None):
            return "0"
        return str(self.like)

    # 自己转成dict对象，方便转成json
    def to_dict(self):
        data = {}
        for f in self._meta.concrete_fields:
            data[f.name] = f.value_from_object(self)
        return data

    def __str__(self):
        return self.title.encode('utf-8')

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.titlePage.storage, self.titlePage.path
        # Delete the model before the file
        super(Articles, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

    class Meta:
        # managed = False
        db_table = 'articles'

# class Life(models.Model):
#     titlePage = models.ImageField(upload_to='live/')
#     title = models.TextField( blank=True, null=True)
#     keyword = models.CharField(max_length=100, blank=True, null=True)
#     content = RichTextField()
#     name = models.CharField(max_length=50, blank=True, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     # 展示HTML文本
#     def get_desc(self):
#         html = self.content
#         dr = re.compile(r'<[^>]+>', re.S)
#         dd = dr.sub('', html)
#         if(len(dd) > 300):
#             return dd[0:300] + "..."
#         return dd + "..."


