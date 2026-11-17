from django.shortcuts import render, redirect
from Ad.models import Ad, Category
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from Ad.forms import AdForm
from django.db.models import Q
from typing import Any
from django.db.models.query import QuerySet
from django.core.paginator import Paginator
# Create your views here.




def ad_list(request):
    ad = Ad.objects.filter()
    category = Category.objects.filter()

    if search := request.GET.get("q"):
       ad = ad.filter(Q(title__icontains=search) | Q(description__icontains=search))

    if (category_id := request.GET.get("category")) and category_id.isdigit():
        ad = ad.filter(category_id=category_id)

    paginator = Paginator(ad, 5)
    page_obj = paginator.get_page(request.GET.get("page"))

    query_params = request.GET.copy()
    query_params.pop("page", None)
    filter_params = query_params.urlencode()

    


    return render(request, "ad/list.html", {"page_obj": page_obj, "categories": category, "filter_params": filter_params})




def ad_detail(request, id):
    ad = Ad.objects.get(id=id)

    return render(request, "ad/detail.html", {"ad": ad})

@login_required
def ad_create(request: HttpRequest)-> HttpResponse:
    form = AdForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.instance.author = request.user
        form.save()
        return redirect("detail_list", id=form.instance.pk)

    return render(request, "ad/create.html", {"form": form })

@login_required
def ad_edit(request: HttpRequest, id:int) -> HttpResponse:
    ad = Ad.objects.get(id=id)
    

    if request.user != ad.author:
        messages.error(request, "Это не ваше обьявление")
        return redirect("ad_list")

    form = AdForm(request.POST or None, instance=ad)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("detail_list", id=ad.pk)

    return render(request, "ad/edit.html", {"form": form, "ad": ad})

@login_required
def ad_delete(request: HttpRequest, id:int) -> HttpResponse:
    ad = Ad.objects.get(id=id)

    if request.user != ad.author:
        messages.error(request, "Это не ваше обьявление")
        return redirect("ad_list")

    
    
    if request.method == "POST":
        ad.delete()
        return redirect("ad_list")
    
    return render(request, "ad/delete.html", { "ad": ad})

def signup(request):
    if request.user.is_authenticated:
        return redirect("ad_list")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Добро пожаловать! Аккаунт создан.")
            return redirect("ad_list")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})

@login_required
def my_list(request) -> HttpResponse:
    ads = Ad.objects.filter(author = request.user)
    return render(request, "ad/my_list.html", {"ad": ads})




    


    


