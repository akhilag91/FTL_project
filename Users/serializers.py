from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    real_name = serializers.SerializerMethodField()
    activity_periods = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.uuid

    def get_real_name(self, obj):
        if obj.first_name or obj.last_name:
            return obj.first_name + " " + obj.last_name

    def get_activity_periods(self, obj):        
        return ActivityPeriodSerializer(obj.activity_timings.all(), many=True).data

    class Meta:
        model = User
        fields  = ['id', 'real_name', 'tz', 'activity_periods']


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ActivityPeriod
        fields = ['started_on', 'ended_on']
