from django.contrib import admin
from .models import Author, Book, BorrowRecord, ManagementStaff
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm
from unfold.contrib.filters.admin import (
    RangeDateFilter, RangeDateTimeFilter
)


@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_per_page = 10


@admin.register(Book)
class BookAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('title', 'genre', 'published_date', 'author')
    search_fields = ('title', 'genre')
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_filter = (
        ('genre'),
        ("created_at", RangeDateFilter)
    )
    list_filter_submit = True
    list_per_page = 10


@admin.register(BorrowRecord)
class BorrowRecordAdmin(ModelAdmin):
    list_display = ('user_name', 'book', 'borrow_date', 'return_date')
    search_fields = ('user_name', 'book')
    list_per_page = 10


@admin.register(ManagementStaff)
class ManagementStaffAdmin(ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_per_page = 10
