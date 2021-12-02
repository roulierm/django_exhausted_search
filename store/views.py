from django.core import paginator
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import post_user
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect
from .filters import UserpostFilter
from django.core.exceptions import ValidationError

def post_detail(request, post_id):
    car = get_object_or_404(Userpost, pk = post_id)
    context = {'car':car}
    return render(request, 'store/userpost_detail.html', context)


def home(request):
    context = {}
    return render(request, 'store/home.html', context)

def store(request):
    dealer_list = Dealer.objects.all()
    context = {'dealer_list': dealer_list}
    return render(request, 'store/store.html', context)

def posts(request):
    cars = Userpost.objects.all()
    myFilter = UserpostFilter(request.GET, queryset=cars)
    if myFilter.qs:
        cars = myFilter.qs

    p = Paginator(cars, 9)
    page = request.GET.get('page')
    try:
        cars = p.page(page)
    except PageNotAnInteger:
        cars = p.page(1)
    except EmptyPage:
        cars = p.page(p.num_pages)

    context = {'cars':cars}
    return render(request, 'store/userposts.html', context)

def createPost(request):
    submitted = False
    if request.method == "POST":
        form = post_user(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("posts/")
    else:
        form = post_user
        if 'submitted' in request.GET:
            submitted = True
    context = {'form':form, 'submitted':submitted}
    return render(request, 'store/createpost.html', context)



