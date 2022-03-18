from dataclasses import fields
from . models import Apiusers
from rest_framework import serializers

class ApiUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Apiusers
        fields = {'username','password'}