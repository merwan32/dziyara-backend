from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

class TransportMeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportMean
        fields = ['mean_name', 'icon']


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        fields = ['id', 'user', 'content', 'created_at']

class TouristicSiteSerializer(serializers.ModelSerializer):
    Transport_Mean = TransportMeanSerializer(many=True, read_only=True)
    comments = UserCommentSerializer(many=True, read_only=True)
    class Meta:
        model = TouristicSite
        fields = ['id','site_name', 'site_type', 'description', 'current_stars', 'picture', 'latitude', 'longitude', 'wilaya', 'Working_Time', 'Transport_Mean','comments']

class TouristicMapSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristicSite
        fields = ['site_name', 'latitude', 'longitude', ]


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        fields = '__all__'