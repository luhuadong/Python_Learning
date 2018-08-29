from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from common.models import Users,Types,Goods,Orders,Detail


def loadinfo(request):
    """ 公共信息加载函数 """
    lists = Types.objects.filter(pid=0)
    context = {'typelist':lists}
    return context


def  viporders(request):
    ''' 浏览订单信息 '''
    context = loadinfo(request)
    #获取当前登录者的订单信息
    odlist = Orders.objects.filter(uid=request.session['vipuser']['id'])
    #遍历订单信息，查询对应的详情信息
    for od in odlist:
        delist = Detail.objects.filter(orderid=od.id)
        #遍历订单详情，并且获取对应的商品信息（图片）
        for og in delist:
            og.picname = Goods.objects.only("picname").get(id=og.goodsid).picname
        od.detaillist = delist

    context['orderslist'] = odlist
    return render(request,"web/viporders.html",context)


def odstate(request):
    ''' 修改订单状态 '''
    try:
        oid = request.GET.get("oid",'0')
        ob = Orders.objects.get(id=oid)
        ob.state = request.GET['state']
        ob.save()
        return redirect(reverse('vip_orders'))
    except Exception as err:
        print(err)
        return HttpResponse("订单处理失败！")


def info(request):
    """ 会员中心的个人信息 """
    context = loadinfo(request)

    print(">>>>>>>>>>>>>>")
    print(request.session['vipuser']['id'])
    user = Users.objects.filter(id=request.session['vipuser']['id'])
    print(">>>>>>> %s" %user[0].username)
    #print(user.id)

    context['user'] = user[0]

    return render(request, "web/vipinfo.html", context)


def update(request):
    """ 执行修改会员信息 """
    context = loadinfo(request)

    try:
        ob = Users.objects.get(id=request.session['vipuser']['id'])
        context['user'] = ob
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        ob.sex = request.POST['sex']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.save()
        context['user'] = ob
        print(ob.name)
        #context={"info":"个人信息更新成功！"}
        context['info'] = "个人信息更新成功！"
    except Exception as err:
        print(err)
        #context={"info":"个人信息更新失败！"}
        context['info'] = "个人信息更新失败！"

    print(context['info'])
    return render(request,"web/vipinfo.html", context)



def resetps(request):
    """ 重置密码表单 """
    return HttpResponse("wait...")


def doresetps(request):
    """ 执行重置密码 """
    return HttpResponse("wait...")
