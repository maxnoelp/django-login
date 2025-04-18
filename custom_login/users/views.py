from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterForm, LoginForm, UserProfileForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import User, UserProfile
import logging
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login

logger = logging.getLogger(__name__)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Registrierung erfolgreich – Sie können sich jetzt einloggen."
            )
            return redirect("login")

    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Login erfolgreich")
                return redirect("home")
            else:
                messages.error(request, "Ungültige Zugangsdaten.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def homeview(request):
    return render(request, "home.html", {"user": request.user})


@login_required
def edit(request):
    user = request.user
    try:
        user_profile = user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=user)

    form = UserProfileForm(
        request.POST or None, request.FILES or None, instance=user_profile
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "edit_form.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
