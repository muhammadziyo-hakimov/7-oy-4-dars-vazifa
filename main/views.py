from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product, Course, Student
from .serializers import CategorySerializer, ProductSerializer, CourseSerializer, StudentSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def home(request):
    prods = Product.objects.all()
    prods = ProductSerializer(prods, many=True)

    if request.method == 'POST':
        prod = ProductSerializer(data=request.data)
        if prod.is_valid():
            prod.save()
            return Response({"message": "Product added"}, status=status.HTTP_201_CREATED)
        return Response(prod.errors)

    return Response(prods.data)


@api_view(["PUT", "PATCH"])
def edit_prod(request, pk):
    prod = get_object_or_404(Product, pk=pk)

    ser = ProductSerializer(prod, data=request.data, partial=True)
    if ser.is_valid():
        ser.save()
        return Response({"message": "Product updated"}, status=status.HTTP_200_OK)
    return Response(ser.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['DELETE'])
def del_prod(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    prod.delete()
    return Response({"message": "Product deleted"}, status=status.HTTP_200_OK)              


@api_view(['GET'])
def categories(request):
    cats = Category.objects.all()
    cats = CategorySerializer(cats, many=True)

    return Response(cats.data)


@api_view(['POST'])
def add_cat(request):
    if request.data:
        cat = CategorySerializer(data=request.data)
        if cat.is_valid():
            cat.save()
            return Response({"message": "Category added"}, status=status.HTTP_201_CREATED)
        return Response(cat.errors)
    return Response({"message": "No data"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'PATCH'])
def edit_cat(request, pk):
    cat = get_object_or_404(Category, pk=pk)

    ser = CategorySerializer(cat, data=request.data, partial=True)
    if ser.is_valid():
        ser.save()
        return Response({"message": "Category updated"}, status=status.HTTP_200_OK)
    return Response(ser.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['DELETE'])
def del_cat(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    cat.delete()
    return Response({"message": "Category deleted"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def courses(request):
    courses = Course.objects.all()
    courses = CourseSerializer(courses, many=True)

    return Response(courses.data)


@api_view(['POST'])
def add_course(request):
    if request.data:
        course = CourseSerializer(data=request.data)
        if course.is_valid():
            course.save()
            return Response({"message": "Course added"}, status=status.HTTP_201_CREATED)
        return Response(course.errors)
    return Response({"message": "No data"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'PATCH'])
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)

    ser = CourseSerializer(course, data=request.data, partial=True)
    if ser.is_valid():
        ser.save()
        return Response({"message": "Course updated"}, status=status.HTTP_200_OK)
    return Response(ser.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['DELETE'])
def del_course(request, pk):    
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return Response({"message": "Course deleted"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def students(request):
    students = Student.objects.all()
    students = StudentSerializer(students, many=True)

    return Response(students.data)

@api_view(['POST'])
def add_student(request):
    if request.data:
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response({"message": "Student added"}, status=status.HTTP_201_CREATED)
        return Response(student.errors)
    return Response({"message": "No data"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'PATCH'])
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    ser = StudentSerializer(student, data=request.data, partial=True)
    if ser.is_valid():
        ser.save()
        return Response({"message": "Student updated"}, status=status.HTTP_200_OK)
    return Response(ser.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['DELETE'])
def del_student(request, pk):    
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return Response({"message": "Student deleted"}, status=status.HTTP_200_OK)