# encoding:utf-8

from django.shortcuts import render
from models import *
import json
from django.core.paginator import *
from django.core import serializers
from django.http import HttpResponse
from joke import Joke
from django.views.decorators.cache import cache_page

@cache_page(60 * 60 * 24 * 1 ) # 缓存一天
def index(request):

    # 首页博客数据
    page = request.GET.get('page')
    qureyList = Articles.objects.order_by('-created_at')
    p = Paginator(qureyList,4)
    if page == None:
        page = '1'
    has_next = False
    has_pre = False
    list2 = []
    nextPage = 0
    prevPage = 0
    try:
        pIndex = int(page)
        list2 = p.page(pIndex)
        has_next = list2.has_next()
        has_pre = list2.has_previous()
        nextPage = pIndex + 1
        prevPage = pIndex - 1
    except Exception as ret:
        pass



    # 首页生活数据
    live = Articles.objects.filter(keyword="生活").order_by('-created_at')
    pLive = Paginator(live, 4)
    listLive = pLive.page(1)


    # 首页笑话
    joke = Joke()

    joke_data = joke.get_joke()
    # return HttpResponse(joke_data)

    contex = {
        'dataList': list2,
        'has_next': has_next,
        'has_pre': has_pre,
        'nextPage': nextPage,
        'prevPage': prevPage,
        'jsonData': serializers.serialize("json",list2),
        'liveList': listLive,
        'joke': joke_data,
    }

    return render(request,'myBlog/index.html',contex)

def comment(request):
    return render(request,'myBlog/comment.html')

@cache_page(60 * 60 * 24 * 1 ) # 缓存一天
def program(request):
    qureyList = Articles.objects.filter(keyword="编程").order_by("-created_at")
    contex = {
        'dataList': qureyList,
        'jsonData': serializers.serialize("json", qureyList),
    }
    return render(request, 'myBlog/program.html', contex)

@cache_page(60 * 60 * 24 * 1 ) # 缓存一天
def detail(request,id):
    data = Articles.objects.filter(id=id)[0]
    last = Articles.objects.last() # 返回的是对象
    first = Articles.objects.first() # 返回的是对象
    has_next = not(int(last.id) == int(id))
    has_pre = not(int(first.id) == int(id))
    # return HttpResponse('fitst: %d - %d'%(has_next,has_pre))

    next_id = None
    pre_id = None
    pre_title = None
    next_title = None
    if has_next:
        nextSet = Articles.objects.filter(id__gt=id)
        if len(nextSet):
            next_id = nextSet.first().id
            next_title = nextSet.first().title
    if has_pre:
        pre_set = Articles.objects.filter(id__lt=id)
        if len(pre_set):
            pre_id = pre_set.first().id
            pre_title = pre_set.first().title
    contex = {
        'item': data,
        'has_next': has_next,
        'has_pre': has_pre,
        'next_id': next_id,
        'pre_id': pre_id,
        'pre_title':pre_title,
        'next_title': next_title,
        'detailUrl': 'detail',
    }
    return render(request,'myBlog/detail.html',contex)

@cache_page(60 * 60 * 24 * 1 ) # 缓存一天
def blog(request):
    qureyList = Articles.objects.filter(keyword="博客").order_by("-created_at")
    contex = {
        'dataList': qureyList,
        'jsonData': serializers.serialize("json", qureyList),
    }
    return render(request, 'myBlog/program.html', contex)

@cache_page(60 * 60 * 24 * 1 ) # 缓存一天
def life(request):

    queryList = Articles.objects.filter(keyword="生活").order_by("-created_at")
    contex = {
        'dataList': queryList,
    }
    return render(request,'myBlog/life.html',contex)

@cache_page(60 * 60 * 24 * 1 ) # 缓存一天
def resume(request):
    return render(request,'myBlog/resume.html')

