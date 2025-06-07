from django.http import HttpResponse

def home(request):
    return HttpResponse(
        "<h1>Bienvenue !</h1><p>L’inscription et la connexion fonctionnent.</p>"
    )
