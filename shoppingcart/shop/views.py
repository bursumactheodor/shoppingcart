from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Produs
from .models import Prodselectat
from  .models import Tip



def home(request):
     return render(request,"shop/home.html")


def tip_list(request):
     obiecte = Tip.objects.all()
     return render(request, "shop/tipuri.html", {'products': obiecte})


def prod_tip_list(request,idp):
     obiecte = Produs.objects.all().filter(tip=idp)
     return render(request, "shop/produsedintip.html", {'products': obiecte})

def product_list(request):
     obiecte = Produs.objects.all()
     return render(request, "shop/product_list.html", {'products': obiecte })


def product_list_tip(request, idtip):
     obiecte = Produs.objects.all().filter(tip=idtip)
     return render(request, "shop/product_list.html", {'products': obiecte })

def product_list_nume(request, num):
     obiecte = Produs.objects.all().filter(nume=num)
     return render(request, "shop/product_list.html", {'products': obiecte })


def product_detalii(request, idp):
     obiecte = Produs.objects.all().filter(id=idp)
     return render(request, "shop/product_detalii.html", {'products': obiecte })

def product_select(request, idp):
     p = Produs.objects.get(id=idp)
     ps=Prodselectat()
     ps.idp=p.id
     ps.tip=p.tip
     ps.nume=p.nume
     ps.pret=p.pret
     ps.cantitate=1
     ps.save()

     obiecte = Prodselectat.objects.all()
     s=0
     for o in obiecte:
          s=s+o.cantitate*o.pret

     return render(request, "shop/product_select.html", {'products': obiecte ,'total': s})


def stergeselectie(request,ids):
    Prodselectat.objects.all().filter(id=ids).delete()
    return redirect("produse/select")
