from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import status
from rest_framework.reverse import reverse
from books.models import Book, Member, Order, BookCategory
from books.serializer import (BookSerializer,
                              MemberSerializer,
                              OrderBookSerializer,
                              BookCategorySerializer,
                              MemberSerializerModel,
                              BookSerializerModel,
                              OrderBookSerializerModel,
                              )
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
import email.utils as eut
import datetime


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def Login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Provide both username or password'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        books_serializer = BookSerializerModel(books, many=True)
        return Response({'error': False,
                         'data': books_serializer.data, 'count': len(books_serializer.data)},
                        status=status.HTTP_200_OK)
    elif request.method == 'POST':
        book_serializer = BookSerializerModel(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response({'error': False,
                             'data': 'Success Saving book - `{}`'.format(request.data.get('title'))},
                            status=status.HTTP_201_CREATED)
        return Response({'error': True,
                         'data': 'Error - {}'.format(book_serializer.errors)},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        book_serializer = BookSerializerModel(book)
        return Response({'error': False,
                         'data': book_serializer.data},
                        status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        book_serializer = BookSerializerModel(book,
                                              data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response({'error': False, 'data': 'success update `pk = {}`'.format(pk)})
        return Response(book_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def member_list(request):
    if request.method == 'GET':
        members = Member.objects.all()
        members_serializer = MemberSerializerModel(members, many=True)
        if not members_serializer:
            return Response({'error': True,
                             'data': 'Not Found'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': False,
                         'data': members_serializer.data},
                        status=status.HTTP_200_OK)

    elif request.method == 'POST':
        member_serializer = MemberSerializerModel(data=request.data)
        if member_serializer.is_valid():
            member_serializer.save()
            return Response({'error': False,
                             'data': 'Success Saving Member `{}`'.format(request.data.get('name'))},
                            status=status.HTTP_201_CREATED)
        return Response({'error': True,
                         'data': 'Error - {}'.format(member_serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def member_detail(request, pk):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return Response({'error': True, 'data': 'Data Not Found pk = {}'.format(pk)}, status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        member_serializer = MemberSerializerModel(member)
        return Response({'error': False,
                         'data': member_serializer.data},
                        status=status.HTTP_200_OK)
    if request.method == 'PUT':
        member_serializer = MemberSerializerModel(member, data=request.data)
        if member_serializer.is_valid():
            member_serializer.save()
            return Response({'error': False,
                             'data': 'success edit id member {}'.format(member_serializer.data['pk'])},
                            status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        member.delete()
        return Response({'error': False, 'data': 'Success delete pk = {}'.format(pk)})


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        orders_serializer = OrderBookSerializerModel(orders, many=True)
        if orders_serializer:
            return Response({'error': False, 'data': orders_serializer.data}, status=status.HTTP_200_OK)
        return Response({'error': True, 'data': 'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        book_title = Book.objects.get(pk=request.data.get('book'))
        member_name = Member.objects.get(pk=request.data.get('member'))
        order_serializer = OrderBookSerializerModel(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(
                {'error': False,
                 'data': 'success saving order book `{}` - member `{}` - booking_code - `{}`'.format(book_title,
                                                                                                     member_name,
                                                                                                     order_serializer.data[
                                                                                                         'code_borrow']
                                                                                                     ),
                 'order_serializer': order_serializer.data},
                status=status.HTTP_201_CREATED)
        return Response({'error': True, 'data': order_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': True, 'data': 'Data Not Found `{}`'.format(pk)})

    if request.method == 'GET':
        order_serializer = OrderBookSerializerModel(order)
        return Response({'error': False,
                         'data': order_serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        order_serializer = OrderBookSerializerModel(order, data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response({'error': False,
                             'data': 'Success Update `{}`'.format(pk)},
                            status=status.HTTP_200_OK)
        return Response({'error': True,
                         'data': 'error - {}'.format(order_serializer.error_messages)})

    elif request.method == 'DELETE':
        order.delete()
        return Response({'error': False,
                         'data': 'success delete - {}'.format(pk)},
                        status=status.HTTP_200_OK)


# GENERIC VIEW
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
    permission_classes = (IsAuthenticated,)
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    name = 'bookcategory-list'


class BookList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    name = 'member-list'
    permission_classes = (IsAuthenticated,)


class OrderList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
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
