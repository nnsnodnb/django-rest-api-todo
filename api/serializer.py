from rest_framework import serializers
from .models import ApiTask

class ApiTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiTask
        fields = ('id', 'title', 'schedule_date', 'finish_date', 'rank', 'finish_check')
