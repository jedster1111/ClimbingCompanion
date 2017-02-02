from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Coder, Climb
from logbook.serializers import ClimbSerializer

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def climb_list(request):
    # List all climbs, or make a new one
    if request.method == 'GET':
        climbs = Climb.objects.all()
        serializer = ClimbSerializer(climbs, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClimbSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=401)

@csrf_exempt
def climb_detail(request, pk):
    try:
        climb = Climb.objects.get(pk=pk)
    except Climb.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ClimbSerializer(climb)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().pasrse(request)
        serializer = ClimbSerializer(climb, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors)
    
    elif request.method == 'DELETE':
        climb.delete()
        return HttpResponse(status=204)



def index(request):
    coder_list = Coder.objects.all()
    context = {'coder_list':coder_list,}
    return render(request,'logbook/index.html', context)