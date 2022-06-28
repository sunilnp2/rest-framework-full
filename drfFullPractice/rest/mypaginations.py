from email.policy import default
from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 7


# pagination for offset pagination
from rest_framework.pagination import LimitOffsetPagination
class MyOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 7


# pagination for cursor pagination
from rest_framework.pagination import CursorPagination
class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'name'