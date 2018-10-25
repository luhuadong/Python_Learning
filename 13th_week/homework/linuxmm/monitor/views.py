from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from monitor.models import Host

# Create your views here.

def index(request, pIndex=1):
    ''' 监控中心-首页 '''

    #return HttpResponse("Hello, world. You're at the myapp index.")

    #hostList = Host.objects.all()
    hostList = Host.objects.get_queryset().order_by('id')

    # 分页
    p = Paginator(hostList, 10)
    if pIndex == "":
        pIndex = "1"
    aList = p.page(pIndex)
    pList = p.page_range
    pNum  = p.num_pages
    context = {"hostlist": aList, "pList": pList, "pIndex": int(pIndex), "pNum":int(pNum)}
    print('-'*12)
    print(context)

    return render(request, "monitor/index.html", context)


def details(request):
    return render(request, "monitor/details.html")

def manual(request):
    return render(request, "monitor/manual.html")

def settings(request):
    return render(request, "monitor/settings.html")