from django.shortcuts import render
from django.urls import reverse
from .models import *

# Create your views here.
def home(request):
    cards=Card.objects.all()
    # tests=test.objects.create(title='test',video='test batafsil')
    # tests.save()
    return render(request, 'index.html', {'cards':cards})

def mavzular(request,title):
    card=Card.objects.get(title=title)
    card=Card.objects.update
    if request.user.is_authenticated:
        return render(reverse('users:login'))
    return render(request, 'mavzular.html', {'card':card})