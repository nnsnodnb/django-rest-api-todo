from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, filters
from .models import ApiTask
from .serializer import ApiTaskSerializer
import django_filters
import json

class ApiTaskViewSet(viewsets.ModelViewSet):
    queryset = ApiTask.objects.all()
    serializer_class = ApiTaskSerializer
    filter_fields = ('id', 'rank', 'finish_check')

    def forbidden(self):
        forbidden_response = json.dumps({'error': '403 Forbidden'})
        response = HttpResponse(forbidden_response, content_type='application/json', status = 403)
        response['Content-Length'] = len(forbidden_response)
        return response

    def create(self, request):
        return self.forbidden()

    def update(self, request, pk = None):
        return self.forbidden()

    def partial_update(self, request, pk = None):
        return self.forbidden()

    def destroy(self, request, pk = None):
        return self.forbidden()
