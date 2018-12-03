from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework import status
from rest_framework.reverse import reverse
from books.models import Book, Member, Order, BookCategory
from books.serializer import BookSerializer, MemberSerializer, OrderBookSerializer, BookCategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        books_serializer = BookSerializer(books, many=True)
        return Response(books_serializer.data)
    elif request.method == 'POST':
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        book_serializer = BookSerializer(book)
        return Response(book_serializer.data)

    elif request.method == 'PUT':
        book_serializer = BookSerializer(book, data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def member_list(request):
    if request.method == 'GET':
        members = Member.objects.all()
        members_serializer = MemberSerializer(members, many=True)
        return Response(members_serializer.data)

    elif request.method == 'POST':
        member_serializer = BookSerializer(data=request.data)
        if member_serializer.is_valid():
            member_serializer.save()
            return Response(member_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        orders_serializer = OrderBookSerializer(orders, many=True)
        return Response(orders_serializer.data, status=status.HTTP_200_OK)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    name = 'member-detail'


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderBookSerializer
    name = 'order-detail'


class BookCategoryList(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    name = 'bookcategory-list'


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    name = 'member-list'


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderBookSerializer
    name = 'order-list'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'bookcategory-list': reverse(BookCategoryList.name, request=request),
            'book-list': reverse(BookList.name, request=request),
            'order-list': reverse(OrderList.name, request=request),
            'member-list': reverse(MemberList.name, request=request)
        })
# Create your views here.
# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
#
# @csrf_exempt
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         books_serializer = BookSerializer(books, many=True)
#         return JSONResponse(books_serializer.data)
#
#     elif request.method == 'POST':
#         book_data = JSONParser().parse(request)
#         book_serializer = BookSerializer(data=book_data)
#         if book_serializer.is_valid():
#             book_serializer.save()
#             return JSONResponse(book_serializer.data, status=status.HTTP_201_CREATED)
#         return JSONResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @a
# def book_detail(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         book_serializer = BookSerializer(book)
#         return JSONResponse(book_serializer.data)
#     elif request.method == 'PUT':
#         book_data = JSONParser().parse(request)
#         book_serializer = BookSerializer(book, data=book_data)
#         if book_serializer.is_valid():
#             book_serializer.save()
#             return JSONResponse(book_serializer.data, status=status.HTTP_200_OK)
#         return JSONResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         book.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
