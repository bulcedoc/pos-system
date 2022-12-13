from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from django.views.decorators.csrf import csrf_exempt
pro = []
quan = []
proud = []
price = []
t_p = []

@csrf_exempt
def see(request):

    if request.method=="POST":
        global pro
        global quan
        pro = (request.POST.get('p',None)).split(',')
        quan = (request.POST.get('q')).split(',')
    return HttpResponse(pro+quan)

def che(request):
    for n in pro:
     proud.append( Products.objects.filter(p_name=n).values('p_price'))
    i=0
    while i<len(pro):
       price.append(proud[i][0]['p_price'])
       i=i+1
    i=0
    while i<len(pro):
       t_p.append(int(quan[i])*int(price[i]))
       i=i+1
    i=0
    total = 0
    while i<len(pro):
       total = total + t_p[i]
       i=i+1
    dic = {}
    i=0
    while i<len(pro):
        dic.update({pro[i]:[int(quan[i]),price[i],t_p[i]]})
        i=i+1
    print(dic)
    context = {
        'p':dic,
        'total':total,
        'c':{"a":"apple"}
    }

    return render(request,'bill.html',context)


def home(request):
    produ = Products.objects.all()
    context = { 
               'products':produ,
              }
    return render(request,'home.html',context)

