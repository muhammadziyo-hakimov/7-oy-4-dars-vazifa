from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
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


