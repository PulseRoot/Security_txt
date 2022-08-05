from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views
from .serializers import *
from .gethost import hostlists
from .parsing import Parsing
import json

class viruslistView(APIView):
    def post(self, request):
        data = []
        username = request.data
        hostlist = hostlists(username)
        for host in hostlist:
            data.append({
                "hostname" : host,
                "virus" : Parsing(username, host),
                "virus_sum" : len(Parsing(username,host))
            })
        json_data = json.dumps(data)
        #serializer = ViruscountSerializer(json)
        #result = json.loads(json_data)
        return Response(data)