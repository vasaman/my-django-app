from django.shortcuts import render
from .models import bus,passenger,busstand

# Create your views here.

def index(request):
    return render(request,"bus/index.html",{
        'buses':bus.objects.all()
    })

def buses(request,bid):
    b=bus.objects.get(id=bid)

    return render(request,"bus/mybus.html",{
        'bus':b,
        'passengers':b.passenger.all()
    })