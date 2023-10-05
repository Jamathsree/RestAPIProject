from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Schoolapp.forms import Schoolform
from Schoolapp.models import Student
from Schoolapp.serializer import Studentserializer

# Create your views here.
def school(request):
    form=Schoolform()
    if request.method=='POST':
        form=Schoolform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'Home.html',{'form':form})

@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = Studentserializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExit:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = Studentserializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Studentserializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
