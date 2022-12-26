from django.shortcuts import render

# Create your views here.

import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Firm, Product, Category
from .serializers import FirmSerializers, ProductSerializers, CategorySerializers


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers


# class FirmCreateListView(generics.ListCreateAPIView):
#     queryset = Firm.objects.all()
#     serializer_class = FirmSerializers

#
# class FirmRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Firm.objects.all()
#     serializer_class = FirmSerializers

@api_view(['POST', 'GET'])
def create_firm(request):
    if request.method == 'POST':
        serializers = FirmSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        firm = Firm.objects.all()
        serializers = FirmSerializers(instance=firm, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_firm(request, pk):
    firm = generics.get_object_or_404(Firm, pk=pk)
    if request.method == 'GET':
        serializer = FirmSerializers(instance=firm)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = FirmSerializers(instance=firm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        firm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def create_category(request):
    if request.method == 'POST':
        serializers = CategorySerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        category = Category.objects.all()
        serializers = CategorySerializers(instance=category, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_category(request, pk):
    category = generics.get_object_or_404(Firm, pk=pk)
    if request.method == 'GET':
        serializer = CategorySerializers(instance=category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = CategorySerializers(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def create_product(request):
    if request.method == 'POST':
        serializers = ProductSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        product = Product.objects.all()
        serializers = ProductSerializers(instance=product, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_product(request, pk):
    product = generics.get_object_or_404(Firm, pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializers(instance=product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = ProductSerializers(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
