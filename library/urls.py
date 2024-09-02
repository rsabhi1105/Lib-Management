from django.urls import path

from . import views
from .views import (
    AuthorListView, AuthorCreateView,
    BookListView, BookCreateView,
    BorrowRecordListView, BorrowRecordCreateView
)

urlpatterns = [

    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('borrow-records/', BorrowRecordListView.as_view(), name='borrowrecord-list'),
    path('authors/add/', AuthorCreateView.as_view(), name='add-author'),
    path('books/add/', BookCreateView.as_view(), name='add-book'),
    path('borrow-records/add/', BorrowRecordCreateView.as_view(), name='add-borrow-record'),

    # to download excel file
    path('export_to_excel/', views.export_to_excel, name='export_to_excel'),

]
