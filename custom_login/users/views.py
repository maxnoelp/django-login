from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth import login


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration successful")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


# Create your views here.
