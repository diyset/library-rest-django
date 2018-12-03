from rest_framework import serializers
from books.models import Book, BookCategory, Member, Order


class BookSerializer(serializers.HyperlinkedModelSerializer):
    book_category = serializers.SlugRelatedField(queryset=BookCategory.objects.all(), slug_field='name')
    url = serializers.HyperlinkedIdentityField(view_name='book-detail')

    class Meta:
        model = Book
        fields = ('pk', 'title', 'publisher', 'publishdate', 'book_category', 'url')


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='member-detail')

    class Meta:
        model = Member
        fields = ('pk', 'name', 'email', 'notelp', 'url')


class BookCategorySerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail'
    )

    class Meta:
        model = BookCategory
        fields = ('pk', 'name', 'books')


class OrderBookSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='title')
    member = serializers.SlugRelatedField(queryset=Member.objects.all(), slug_field='name')
    url = serializers.HyperlinkedIdentityField(view_name='order-detail')

    class Meta:
        model = Order
        fields = (
            'pk',
            'book',
            'member',
            'date_borrow',
            'due_date',
            'url',
        )
