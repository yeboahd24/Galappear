from django.shortcuts import render
from .models import Gaming, Abstract, Logo


def index(request):
    abstracts = Abstract.objects.all()

    return render(request, 'index.html', {"abstracts": abstracts})


def gaming(request):
    gamings = Gaming.objects.all()

    return render(request, 'gaming.html', {'gamings': gamings})


def logo(request):
    logos = Logo.objects.all()

    return render(request, 'logos.html', {'logos': logos})
