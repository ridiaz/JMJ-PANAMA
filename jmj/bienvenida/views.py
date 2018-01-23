from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hola JMJ 2019 !!!</h1>")