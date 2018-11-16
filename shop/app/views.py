from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
import uuid
from datetime import datetime
from django.template import Template
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import logout_then_login
from django.contrib.sessions.models import Session
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core import validators
from django.utils.translation import ugettext as _
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app.forms import*
from app.models import*
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
import json



def registration(request):
    flag= False
    if request.method == "POST":
        form = AdminUserForm(request.POST)
        if form.is_valid():
            user_obj = form.save(request)
            user_obj.is_superuser = 0
            user_obj.is_staff = 0
            user_obj.is_active = 1
            user_obj.save()
            form = AdminUserForm()
            success = "success"
            try:
                password = request.session["password"]
                del request.session["password"]
            except:
                password = None
            user_type= request.POST.get('user_type')
            return render(request, 'registration.html', {
        'form':form,"success":True
    })
    else:
        form = AdminUserForm()
    return render(request, 'registration.html', {
        'client':True,'form':form,'flag':flag
    })




def login(request, template_name):
    if request.user.is_authenticated():
        return loginredirect(request)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = get_object_or_404(User, pk=form.get_user_id())
            loginuser = form.get_user()
            if loginuser is not None:
                if loginuser.is_active:
                    auth_login(request, loginuser)
                    if request.GET.get('next'):
                        return HttpResponseRedirect(request.GET.get('next'))
                else:
                    errors='activate account through mail'
            return loginredirect(request)
            #return HttpResponseRedirect('/home/')
    else:
        form = AuthenticationForm()
        try:
            msg = request.session['activation_msg']
            del request.session['activation_msg']
        except:
            pass
    return render(request,template_name, locals())

def loginredirect(request):
    user = request.user
    return HttpResponseRedirect('/')  #dashboard
def logout_page(request):
    return logout_then_login(request)


@login_required
def customer_dashboard(request):
     current_user = request.user
     return HttpResponseRedirect('/business_profile/')


     return render(request, 'customer_dashboard.html', {
       'data':'coming soon'})

@csrf_exempt
def product_view(request):
    obj = add_product.objects.values("product_Id","Productname","price","stock","imageurl","category","unit","colour")
    return HttpResponse(json.dumps(list(obj)))

@csrf_exempt
def cart_view(request):
    if request.method == "GET":
        if str(request.user) == "AnonymousUser":
            return HttpResponse(json.dumps({"auth":"fail"}))
        print(request.GET.get)
        obj = add_cart()
        obj.product_Id = request.GET.get("product_Id")
        obj.quantity = request.GET.get("quantity")
        obj.user = request.user
        obj.created_date = str(datetime.now())
        obj.created_by = request.user
        obj.save()
        return HttpResponse(json.dumps({"status":"sucess"}))
    return HttpResponse(json.dumps({"status":"fail"}))

@csrf_exempt
def cart_view_data(request):
    obj = add_cart.objects.filter(user=request.user)
    dct = {}
    lst = []
    for i in obj:
        dct = {}
        dct["product_Id"] = i.product_Id
        dct["quantity"] = i.quantity
        ob = add_product.objects.get(product_Id=i.product_Id)
        dct["Productname"] = ob.Productname
        dct["price"] = ob.price
        dct["imageurl"] = str(ob.imageurl)
        dct["colour"] = ob.colour
        lst.append(dct)
    return HttpResponse(json.dumps(list(lst)))

def login_status(request):
    if request.user.is_authenticated():
        return HttpResponse(json.dumps({"status":"True"}))
    return HttpResponse(json.dumps({"status":"False"}))
