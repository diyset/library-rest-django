from django.urls import path
from books import views

urlpatterns = [
    path('book/', views.book_list),
    path('books/', views.BookList.as_view(), name=views.BookList.name),
    path('books/<int:pk>/', views.BookDetail.as_view(), name=views.BookDetail.name),
    path('book/<int:pk>/', views.book_detail),
    path('member/', views.member_list),
    path('members/', views.MemberList.as_view(), name=views.MemberList.name),
    path('members/<int:pk>/', views.MemberDetail.as_view(), name=views.MemberDetail.name),
    path('order/', views.order_list),
    path('orders/', views.OrderList.as_view(), name=views.OrderList.name),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name=views.OrderDetail.name),
    path('category/', views.BookCategoryList.as_view(), name=views.BookCategoryList.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

]
