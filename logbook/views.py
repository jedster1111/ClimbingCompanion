from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics

# class based view
from rest_framework.views import APIView

from .models import Coder, Climb
from logbook.serializers import ClimbSerializer

class ClimbList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView,):
    queryset = Climb.objects.all()
    serializer_class = ClimbSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class ClimbDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Climb.objects.all()
    serializer_class = ClimbSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



def index(request):
    coder_list = Coder.objects.all()
    context = {'coder_list':coder_list,}
    return render(request,'logbook/index.html', context)