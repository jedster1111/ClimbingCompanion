from django.shortcuts import render
from .models import Coder

# Create your views here.

def index(request):
    coder_list = Coder.objects.all()
    context = {'coder_list':coder_list,}
    return render(request,'logbook/index.html', context)