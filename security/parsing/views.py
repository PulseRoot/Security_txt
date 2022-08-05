from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views
from .serializers import *
from .gethost import hostlists
from .parsing import Parsing

class viruslistView(APIView):
    def post(self, request):
        
        username = request.data
        serializer = ViruscountSerializer(username)

        return Response(serializer.data)