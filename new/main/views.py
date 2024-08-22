
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Это главная страница</h1>")
def data(request):
    return HttpResponse("<h1>Это страница data</h1>")

def test(request):
    return HttpResponse("<h1>Это страница test</h1>")
