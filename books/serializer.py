from rest_framework import serializers
from books.models import Book, BookCategory, Member, Order
from django.utils import timezone
import datetime


class BookSerializer(serializers.HyperlinkedModelSerializer):
    book_category = serializers.SlugRelatedField(queryset=BookCategory.objects.all(), slug_field='name')
    url = serializers.HyperlinkedIdentityField(view_name='book-detail')

    class Meta:
        model = Book
        fields = ('pk', 'title', 'publisher', 'publishdate', 'book_category', 'url',)


class BookSerializerModel(serializers.ModelSerializer):
    publishdate = serializers.DateTimeField(format='%d-%m-%Y', default=timezone.now(), input_formats='%m-%d-%Y')

    class Meta:
        model = Book
        fields = ('pk', 'title', 'publisher', 'publishdate', 'book_category',)


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='member-detail')

    class Meta:
        model = Member
        fields = ('pk', 'name', 'email', 'notelp', 'url', 'gender')


class MemberSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('pk', 'name', 'email', 'notelp', 'gender')


class BookCategorySerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail'
    )

    class Meta:
        model = BookCategory
        fields = ('pk', 'name', 'books')


class OrderBookSerializerModel(serializers.ModelSerializer):
    date_borrow = serializers.DateTimeField(default=datetime.datetime.now(), format='%m-%d-%Y')
    due_date = serializers.DateTimeField(format='%m-%d-%Y', input_formats=['%m-%d-%Y'])

    class Meta:
        model = Order
        fields = ('pk', 'book', 'member', 'date_borrow', 'due_date', 'code_borrow')


class OrderBookSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='title')
    member = serializers.SlugRelatedField(queryset=Member.objects.all(), slug_field='name')
    url = serializers.HyperlinkedIdentityField(view_name='order-detail')
    due_date = serializers.DateTimeField(format="'%m-%d-%Y", required=True)
    date_borrow = serializers.DateTimeField(format='%m-%d-%Y')

    class Meta:
        model = Order
        fields = (
            'pk',
            'book',
            'member',
            'date_borrow',
            'due_date',
            'url',
            'code_borrow'
        )
