# encoding:utf-8

from django.shortcuts import render
from models import *
import json
from django.core.paginator import *
from django.core import serializers
from django.http import HttpResponse
from joke import Joke
from django.views.decorators.cache import cache_page

#@cache_page(60 * 60 * 24 * 1 ) # 缓存一天
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


def mo(request):
    str= {"status": "1", "data": {"province": "江苏省", "cross_list": [
        {"distance": "191.482", "direction": "West", "name": "联谊路--绿溪路", "weight": "120", "level": "45000, 45000",
         "longitude": "121.0512567", "crossid": "021H51F0090093015--021H51F009009851", "width": "8, 8",
         "latitude": "31.31579861"},
        {"distance": "233.802", "direction": "NorthEast", "name": "陆家浜南路--绿溪路", "weight": "120",
         "level": "45000, 45000", "longitude": "121.0476761", "crossid": "021H51F00900930--021H51F009009851",
         "width": "8, 8", "latitude": "31.31397833"},
        {"distance": "233.802", "direction": "NorthEast", "name": "陆家浜南路--陆家浜北路", "weight": "120",
         "level": "45000, 45000", "longitude": "121.0476761", "crossid": "021H51F00900930--021H51F0090093005",
         "width": "8, 8", "latitude": "31.31397833"}], "code": "1", "tel": "0512", "cityadcode": "320500",
                               "areacode": "0512", "timestamp": "1513221306.9", "sea_area": {"adcode": "", "name": ""},
                               "pos": "在陆家镇人民政府附近, 在绿溪路旁边, 靠近联谊路--绿溪路路口", "road_list": [
            {"distance": "78", "direction": "NorthWest", "name": "绿溪路", "level": "5", "longitude": "121.05",
             "width": "8", "roadid": "021H51F009009851", "latitude": "31.315"},
            {"distance": "148", "direction": "SouthEast", "name": "教堂路", "level": "5", "longitude": "121.048",
             "width": "4", "roadid": "021H51F0090092871", "latitude": "31.3163"},
            {"distance": "191", "direction": "West", "name": "联谊路", "level": "5", "longitude": "121.051", "width": "8",
             "roadid": "021H51F0090093015", "latitude": "31.3158"}], "result": "true", "message": "Successful.",
                               "desc": "江苏省,苏州市,昆山市", "city": "苏州市", "districtadcode": "320583", "district": "昆山市",
                               "country": "中国", "provinceadcode": "320000", "version": "2.0-3.0.7339.1438",
                               "adcode": "320583", "poi_list": [
            {"parent": "", "distance": "156", "direction": "West", "tel": "0512-57877735;0512-57671209",
             "name": "昆山市第四人民医院", "weight": "0.0", "typecode": "090100", "childtype": "", "longitude": "121.047609",
             "towards_angle": "", "f_nona": "other", "address": "陆家浜北路21号", "latitude": "31.315540",
             "entrances": [{"latitude": "31.314923", "longitude": "121.047078"}], "end_poi_extension": "2",
             "type": "医疗保健服务;综合医院;综合医院", "poiid": "B020007Y9K"},
            {"parent": "", "distance": "159", "direction": "West", "tel": "0512-57671209;0512-57879719",
             "name": "昆山市陆家人民医院", "weight": "0.0", "typecode": "090100", "childtype": "", "longitude": "121.047573",
             "towards_angle": "", "f_nona": "other", "address": "陆家镇镇北路21号", "latitude": "31.315535",
             "entrances": [{"latitude": "31.315090", "longitude": "121.046996"}], "end_poi_extension": "2",
             "type": "医疗保健服务;综合医院;综合医院", "poiid": "B020016BMR"},
            {"parent": "", "distance": "139", "direction": "SouthWest", "tel": "0512-57671003", "name": "陆家镇人民政府",
             "weight": "0.0", "typecode": "130105", "childtype": "", "longitude": "121.048458",
             "towards_angle": "153.10", "f_nona": "other", "address": "菉溪路22号", "latitude": "31.314539",
             "entrances": [{"latitude": "31.314413", "longitude": "121.048453"}], "end_poi_extension": "2",
             "type": "政府机构及社会团体;政府机关;乡镇级政府及事业单位", "poiid": "B020007YBU"},
            {"parent": "", "distance": "139", "direction": "SouthWest", "tel": "", "name": "陆家镇人民代表大会", "weight": "0.0",
             "typecode": "130105", "childtype": "", "longitude": "121.048458", "towards_angle": "153.20",
             "f_nona": "other", "address": "菉溪路22号", "latitude": "31.314539", "end_poi_extension": "2",
             "type": "政府机构及社会团体;政府机关;乡镇级政府及事业单位", "poiid": "B020007YBT"},
            {"parent": "", "distance": "139", "direction": "SouthWest", "tel": "", "name": "中共昆山市陆家镇委员会",
             "weight": "0.0", "typecode": "130105", "childtype": "", "longitude": "121.048458",
             "towards_angle": "153.20", "f_nona": "other", "address": "菉溪路22号", "latitude": "31.314539",
             "end_poi_extension": "2", "type": "政府机构及社会团体;政府机关;乡镇级政府及事业单位", "poiid": "B020008HW1"}]}}
    return HttpResponse(json.dumps(str))

