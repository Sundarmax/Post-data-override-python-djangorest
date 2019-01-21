from django.shortcuts import render
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.viewsets import ModelViewSet
from rest_framework import status,views
from rest_framework.decorators import api_view
from rest_framework.response import Response
#model 
from .models import Sections, Ratings
#serializer
from .serializer import sectionSerializer,ratingSerializer
# json
import json
# Create your views here.
from django.http import QueryDict
import os
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'id.txt')
def write(number):
    with open(file_path, 'w') as f:
        f.write('%d' % number)
        f.close()
def read():
    f = open(file_path, 'r')   
    text = f.readline()
    print(text)
    id =  int(text)
    id =  id + 1
    write(id)
    f.close()
    return id

@api_view(['GET','POST','DELETE'])
def Create_Section(request):
    if request.method == 'GET':
        data = Sections.objects.all()
        serializer = sectionSerializer(data,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        myDict = dict(data)
        #data = json.loads(request.data)
        sectionid = read()
        myDict['section_id']= int(sectionid)
        string = ''.join(myDict['title'])
        myDict['title']=string
        description = ''.join(myDict['description'])  
        myDict['description']=description
        qdict = QueryDict('', mutable=True)
        qdict.update(myDict)
        print(request.data)
        print(qdict)
        print(myDict)
        serializer = sectionSerializer(data = qdict )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data = Sections.objects.all()
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)   
        
@api_view(['GET','POST','DELETE'])
def Create_Rating(request):
    if request.method == 'GET':
        data = Ratings.objects.all()
        serializer = ratingSerializer(data,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ratingSerializer(data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data = Ratings.objects.all()
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)   