from dataclasses import field
from unittest import result
from django.forms import JSONField
from rest_framework import serializers
from .models import *
from .gethost import hostlists
from .parsing import Parsing

# 입력값을 받아 알고리즘을 사용하여 계산 후 결과 값 json으로 출력
class ViruscountSerializer(serializers.Serializer):
   virus = serializers.SerializerMethodField(method_name='getVirusList')
   virus_sum = serializers.SerializerMethodField(method_name='countVirus')

   class Meta:
      model = Gethost
      fields = ('username','virus','virus_sum')

   def getVirusList(self, obj):
      username = obj
      viruslist = []
      hostlist = hostlists(username)
      for i in range(len(hostlist)):
         viruslist = Parsing(username, hostlist[i])
         return viruslist

   def countVirus(self, obj):
      username = obj
      viruslist = []
      hostlist = hostlists(username)
      for i in range(len(hostlist)):
         viruslist = Parsing(username, hostlist[i])
         return len(viruslist)

