from django.shortcuts import render
from logbook.models import Centre

def newClimb(request):
    centre_list = Centre.objects.all()
    context = {'centre_list':centre_list,}
    return render(request,'newclimb.html', context)