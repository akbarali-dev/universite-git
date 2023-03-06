from datetime import datetime
from import_export.admin import ImportExportActionModelAdmin
from django.contrib import admin

from .models import Book, User, BookRecord


@admin.register(Book)
class BookAdmin(ImportExportActionModelAdmin):
    search_fields = ("tite", "author")
    list_display = ("tite", "author", "count")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name")
    list_display = ("first_name", "role")
    list_filter = ("role",)


def mark_book_record_as_returned(modeladmin, request, queryset):
    queryset.filter(returned_on__isnull=True).update(returned_on=datetime.today())


@admin.register(BookRecord)
class BookRecordAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "took_on", "is_returned")
    autocomplete_fields = ("book", "user",)  # add select search
    list_select_related = ("book", "user",)
    actions = (mark_book_record_as_returned,)
