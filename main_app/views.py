# unused, only for templating
from django.shortcuts import render
# Create your views here.
# or controllers/controller logic
from rest_framework.views import APIView
from rest_framework.response import Response
# to add the new commands from the urls
from rest_framework import generics
from .models import Cat
from .serializers import CatSerializer

# Define the home view
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the cat-collector api home route!'}
        return Response(content)
    
class CatList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    lookup_field = 'id'    