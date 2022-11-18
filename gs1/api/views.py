from django.shortcuts import render
from .models import Student
# Create your views here.
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializers(stu)
    # with JsonResponce
    return JsonResponse(serializer.data)
    # with httpResponce
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')


def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializers(stu, many=True)
    # with JsonResponce
    return JsonResponse(serializer.data, safe=False)
    # with httpResponce
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')



