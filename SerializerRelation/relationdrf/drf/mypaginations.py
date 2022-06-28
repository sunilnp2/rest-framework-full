from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 2
    max_page_size = 2
    ordering = 'name'