from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.generic import FormView
from .models import BackUpCopy, Tariff, Receipt, TelephoneConversation, Client, User
from .forms import AddBUC, AddTar, AddUser, AddRec, AddTC, AddCl
from django.views import generic
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from LDCCompany import forms

def great(request):
    return render(request, "great.html")

def index(request):
    return render(request, "index.html")

def index_backup(request): #index_author
    form_buc = AddBUC()
    data = BackUpCopy.objects.all()
    return render(request, "LDCCompany/Template_BackUp.html", {"form":form_buc, "data_show":data})

def index_tariff(request): #index_exhibition
    form_t = AddTar()
    data = Tariff.objects.all()
    return render(request, "LDCCompany/Template_Tariff.html", {"form":form_t, "data_show":data})

def index_user(request):
    form_ca = AddUser()
    data = User.objects.all()
    return render(request, "LDCCompany/Template_User.html", {"form":form_ca, "data_show":data})

def index_receipt(request):
    form_r = AddRec()
    data = Receipt.objects.all()
    return render(request, "LDCCompany/Template_Receipt.html", {"form":form_r, "data_show":data})

def index_telephone_conversation(request):
    form_tc = AddTC()
    data = TelephoneConversation.objects.all()
    return render(request, "LDCCompany/Template_Conversation.html", {"form":form_tc, "data_show":data})

def index_client(request):
    form_cl = AddCl()
    data = Client.objects.all()
    return render(request, "LDCCompany/Template_Client.html", {"form":form_cl, "data_show":data})

#Определение view

class view_backup(View):
    def add_backup(request):
        if request.method == "POST":
            backup = BackUpCopy()
            backup.name_of_copy = request.POST.get("name_of_copy")
            backup.type_of_copy = request.POST.get("type_of_copy")
            backup.creation_date = request.POST.get("creation_date")
            backup.commentary = request.POST.get("commentary")
            backup.save()
            return HttpResponseRedirect("/backup")

    def del_backup(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = BackUpCopy.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/backup")

    def update_backup(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = BackUpCopy.objects.get(id=q)
            que.name_of_copy = request.POST.get("name_of_copy")
            que.type_of_copy = request.POST.get("type_of_copy")
            que.creation_date = request.POST.get("creation_date")
            que.commentary = request.POST.get("commentary")
            que.save()
            return HttpResponseRedirect("/backup")

class view_user(View):
    def add_user(request):
        if request.method == "POST":
            user = User()
            user.login = request.POST.get("login")
            user.password = request.POST.get("password")
            user.id_receipt = Receipt.objects.get(id=request.POST.get("id_receipt"))
            user.id_client = Client.objects.get(id=request.POST.get("id_client"))
            user.save()
            return HttpResponseRedirect("/user")

    def del_user(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = User.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/user")

    def update_user(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = User.objects.get(id=q)
            que.login = request.POST.get("login")
            que.password = request.POST.get("password")
            que.id_receipt = Receipt.objects.get(id=request.POST.get("id_receipt"))
            que.id_client = Client.objects.get(id=request.POST.get("id_client"))
            que.save()
            return HttpResponseRedirect("/user")

class view_tariff(View):
    def add_tariff(request):
        if request.method == "POST":
            tariff = Tariff()
            tariff.date = request.POST.get("date")
            tariff.settlment = request.POST.get("settlment")
            tariff.cost_per_minute = request.POST.get("cost_per_minute")
            tariff.preferential_cost = request.POST.get("preferential_cost")
            tariff.save()
            return HttpResponseRedirect("/tariff")

    def del_tariff(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Tariff.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/tariff")

    def update_tariff(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Tariff.objects.get(id=q)
            que.normal_temperature = request.POST.get("normal_temperature")
            que.settlment = request.POST.get("settlment")
            que.cost_per_minute = request.POST.get("cost_per_minute")
            que.preferential_cost = request.POST.get("preferential_cost")
            que.save()
            return HttpResponseRedirect("/tariff")

class view_receipt(View):
    def add_receipt(request):
        if request.method == "POST":
            receipt = Receipt()
            receipt.date = request.POST.get("date")
            receipt.cost = request.POST.get("cost")
            receipt.payment_term = request.POST.get("payment_term")
            receipt.id_tariff = Tariff.objects.get(id=request.POST.get("id_tariff"))
            receipt.id_tconversation = TelephoneConversation.objects.get(id=request.POST.get("id_tconversation"))
            receipt.id_client = Client.objects.get(id=request.POST.get("id_client"))
            receipt.save()
            return HttpResponseRedirect("/receipt")

    def del_receipt(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Receipt.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/receipt")

    def update_receipt(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Receipt.objects.get(id=q)
            que.date = request.POST.get("date")
            que.cost = request.POST.get("cost")
            que.payment_term = request.POST.get("payment_term")
            que.id_tariff = Tariff.objects.get(id=request.POST.get("id_tariff"))
            que.id_tconversation = TelephoneConversation.objects.get(id=request.POST.get("id_tconversation"))
            que.id_client = Client.objects.get(id=request.POST.get("id_client"))
            que.save()
            return HttpResponseRedirect("/receipt")

class view_conversation(View):
    def add_conversation(request):
        if request.method == "POST":
            conversation = TelephoneConversation()
            conversation.date = request.POST.get("date")
            conversation.city = request.POST.get("city")
            conversation.number = request.POST.get("number")
            conversation.call_duration = request.POST.get("call_duration")
            conversation.save()
            return HttpResponseRedirect("/conversation")

    def del_conversation(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = TelephoneConversation.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/conversation")

    def update_conversation(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = TelephoneConversation.objects.get(id=q)
            que.wintering_place = request.POST.get("wintering_place")
            que.city = request.POST.get("city")
            que.number = request.POST.get("number")
            que.call_duration = request.POST.get("call_duration")
            que.save()
            return HttpResponseRedirect("/conversation")

class view_client(View):
    def add_client(request):
        if request.method == "POST":
            client = Client()
            client.number = request.POST.get("number")
            client.firstname = request.POST.get("firstname")
            client.lastname = request.POST.get("lastname")
            client.address = request.POST.get("address")
            client.registration_date = request.POST.get("registration_date")
            client.save()
            return HttpResponseRedirect("/client")

    def del_client(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Client.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/client")

    def update_client(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Client.objects.get(id=q)
            que.number = request.POST.get("number")
            que.firstname = request.POST.get("firstname")
            que.lastname = request.POST.get("lastname")
            que.address = request.POST.get("address")
            que.registration_date = request.POST.get("registration_date")
            que.save()
            return HttpResponseRedirect("/client")
