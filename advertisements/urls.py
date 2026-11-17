"""
URL configuration for advertisements project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Ad.views import ad_create, ad_delete, ad_detail, ad_edit, ad_list, signup, my_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ad_list, name="ad_list"),
    path("ad/detail/<int:id>/", ad_detail, name="detail_list"),
    path("ad/detail/<int:id>/edit/", ad_edit, name="ad_edit"),
    path("ad/detail/<int:id>/delete/", ad_delete, name="ad_delete"),
    path("ad/create/", ad_create, name="ad_create"),
    path("ad/my/", my_list, name="my_list"),
    path("ad/signup", signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),

]
