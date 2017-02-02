from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# class based view
from rest_framework.views import APIView

from .models import Coder, Climb
from logbook.serializers import ClimbSerializer

#class JSONResponse(HttpResponse):
#
#   def __init__(self, data, **kwargs):
#       content = JSONRenderer().render(data)
#       kwargs['content_type'] = 'application/json'
#       super(JSONResponse, self).__init__(content, **kwargs)

#@api_view(['GET','POST'])
#def climb_list(request, format=None):
    #list all climbs or create a new climb
#
#    if request.method == 'GET':
#        climbs = Climb.objects.all()
#        serializer = ClimbSerializer(climbs, many=True)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        serializer = ClimbSerializer(data = request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClimbList(APIView):
    def get(self, request, format = None):
        climbs = Climb.objects.all()
        serializer = ClimbSerializer(climbs, many = True)
        return Response(serializer.data)

    def post(self,request,format = None):
        serializer = ClimbSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class ClimbDetail(APIView):
    def get_object(request, pk):
        try:
            return Climb.objects.get(pk=pk)
        except Climb.DoesNotExist:
            raise Http404

        def get(self, request, pk, format = None):
            serializer = ClimbSerializer(climb)
            return Response(serializer.data)

        def put(self,request,pk,format=None):
            climb = self.get_object(pk)
            serializer = ClimbSerializer(climb, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        def delete(self,request,pk,format = None):
            climb = self.object_get(pk)
            climb.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  


def index(request):
    coder_list = Coder.objects.all()
    context = {'coder_list':coder_list,}
    return render(request,'logbook/index.html', context)