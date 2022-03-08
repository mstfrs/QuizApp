from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import Category, Quiz
from .serializers import CategorySerializer, QuizSerializer
from rest_framework import viewsets


class Categories(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class QuizView(APIView):
   
    def get(self, request, category):
        queryset = Quiz.objects.filter(category=category)
        serializer = QuizSerializer(queryset, many=True)
        return Response(serializer.data)