from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import register, login_view, homeview, edit, logout_view

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("editprofile/", edit, name="editprofile"),
    path("logout/", logout_view, name="logout"),
    path("", homeview, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
