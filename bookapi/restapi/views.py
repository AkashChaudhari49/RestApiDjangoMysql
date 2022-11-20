from django.shortcuts import render
from rest_framework.response import Response
from rest_framework .views import APIView
from rest_framework import status
from .models import Book
from .serializer import BookSerializer

# Create your views here.
class BookDetail(APIView):
    def get(self, request):
        obj = Book.objects.all()
        serializer = BookSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookInfo(APIView):
    def get(self, request,book_id):
        try:
            obj = Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            msg={"msg":"is not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request,book_id):
        try:
            obj = Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            msg={"msg":"is not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)  

        serializer = BookSerializer(obj, data=request.data)

        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,book_id):
        try:
            obj = Book.objects.get(book_id=book_id)
        except Book.DoesNotExist:
            msg={"msg":"is not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg":"deleted record"}, status=status.HTTP_204_NO_CONTENT)