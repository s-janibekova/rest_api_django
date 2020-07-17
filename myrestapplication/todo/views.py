from django.shortcuts import render
from .models import TodoItem
from .serializers import TodoItemSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ToDoListView(APIView):
    def get(self, request):
        items = TodoItem.objects.all()
        serializer = TodoItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)