from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
# Create your views here.

# @api_view(['GET', 'POST'])
# def studentView(request):

#     if request.method =="GET":
#         students = Student.objects.all()
#         serializer  = StudentSerializers(students, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer  = StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


#using class base view

# class StudentView(APIView):

#     def get(self, request, format=None):
#         students = Student.objects.all()
#         serializer  = StudentSerializers(students, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format= None):
#         serializer  = StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# Using mixins and generics views


class StudentView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class  = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# @api_view(['PUT', 'GET', 'DELETE'])
# def studentDetail(request, pk):

#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = StudentSerializers(student)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = StudentSerializers(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# using class base views

# class StudentDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return Http404

#     def get(self, request, pk, format=None):
#         student = self.get_object(pk)
#         serializer = StudentSerializers(student)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         student  =self.get_object(pk)
#         serializer = StudentSerializers(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         student  =self.get_object(pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class  =StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)







        




