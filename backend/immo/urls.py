"""
URL configuration for immo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.conf.urls.static import static


# --- vues minimales ---
def health(request):
    return JsonResponse({"status": "ok"})


def home(request):
    return HttpResponse(
        "<h1>Bienvenue !</h1><p>Votre inscription a réussi et l'application tourne.</p>"
    )


urlpatterns = [
    path("", home, name="home"),                  # page d’accueil
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),   # signup/login/logout
    path("health/", health),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
