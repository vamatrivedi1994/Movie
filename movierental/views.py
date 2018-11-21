from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Customer,CustomerForm,Movie,MovieForm


def available(request):
    movies = Movie.objects.all().filter(rentedby__isnull = True)
    return render(request, "Available.html", {'movies': movies,})

def rented(request):
    movies = Movie.objects.all().filter(rentedby__isnull = False)
    return render(request, "rented.html", {'movies': movies,})

def movies(request):
    movies = Movie.objects.all()
    return render(request, "movies.html", {'movies': movies,})

def customer(request):
    customers = Customer.objects.all()
    return render(request, "customer.html", {'customers': customers,})

def addmovie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            released = form.cleaned_data['released']
            duration = form.cleaned_data['duration']
            price = form.cleaned_data['price']
            genre = form.cleaned_data['genre']
            a = Movie(name=name, released=released, duration=duration, price=price, genre=genre)
            a.save()
            return redirect('/movierental/movies/')
    else:
        form = MovieForm()
    return render(request, "addmovie.html", {'MovieForm': form})

def addcustomer(request):
    formm = CustomerForm(request.POST)
    if formm.is_valid():
        formm.save()
        return redirect('/movierental/customer/')
    return render(request, "addcustomer.html", {'CustomerForm': formm})

def removemovie(request, num):
    object = Movie.objects.get(id = num)
    object.delete()
    return redirect('movies')

def removecustomer(request,num):
    object = Customer.objects.get(id = num)
    object.delete()
    return redirect('customer')
