from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from functools import reduce
# Create your views here.
def home(request):
    return render(request , "pagination/home.html")


class create_List(APIView):
    def get(self , request):
        chars = gameCarecters.objects.all()
        serializer = GameChar_serializer(chars , many=True)
        return Response(serializer.data , status =200)
    def post(self, request, format=None):
        serializer = GameChar2_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class get_delete_update(APIView):
    def delete(self , requets , id):
        try:
            charecter_to_delete = gameCarecters.objects.get(id=id)
            charecter_to_delete.delete() 
            return Response( status = 204)
        except gameCarecters.DoesNotExist:
            return Response({"Error": "the charecter doesn't exist"}, status=400)

    def put(self , request , id ):
        try: 
            instance =  gameCarecters.objects.get(id=id)
            serializer = GameChar_serializer(instance , data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status = 201)
        except gameCarecters.DoesNotExist:
            return Response({"Error": "the charecter doesn't exist"}, status=400)
    def get(self , request , id):
        try:
            charecter = gameCarecters.objects.get(id=id)
            serializer = GameChar_serializer(charecter)
            return Response(serializer.data , status = 200)
        except gameCarecters.DoesNotExist : 
            return Response({"Error": "the charecter doesn't exist"}, status=400)

@api_view(('POST',))
def search_by_name(request):
    if request.method == 'POST':
        try:
            name = request.data["name"]
            name_parts = name.split()
            characters = gameCarecters.objects.filter(
                reduce(lambda q, part: q & Q(name__icontains=part), name_parts, Q()))
            serializer = GameChar_serializer(characters, many=True)
            print(serializer.data)
            return Response(serializer.data, status=200)
        except (KeyError, json.JSONDecodeError):
            return Response({'error': 'Invalid request data'}, status=404)
    else:
        return Response({'error': 'Method not allowed'}, status=405)

