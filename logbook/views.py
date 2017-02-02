from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Coder, Climb
from logbook.serializers import ClimbSerializer

#class JSONResponse(HttpResponse):
#
#   def __init__(self, data, **kwargs):
#       content = JSONRenderer().render(data)
#       kwargs['content_type'] = 'application/json'
#       super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET','POST'])
def climb_list(request, format=None):
    #list all climbs or create a new climb

    if request.method == 'GET':
        climbs = Climb.objects.all()
        serializer = ClimbSerializer(climbs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClimbSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def climb_detail(request, pk, format=None):
    try:
        climb = Climb.objects.get(pk=pk)
    except Climb.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClimbSerializer(climb)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClimbSerializer(climb, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        climb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    coder_list = Coder.objects.all()
    context = {'coder_list':coder_list,}
    return render(request,'logbook/index.html', context)