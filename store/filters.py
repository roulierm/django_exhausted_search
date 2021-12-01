from django.contrib.auth.models import User
import django_filters
from django_filters import DateFilter
from django_filters import NumberFilter
from .models import Userpost

class UserpostFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "date_published", lookup_expr = 'gte')
    end_date = DateFilter(field_name = "date_published", lookup_expr = 'lte')
    min_price = django_filters.NumberFilter(field_name="Price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="Price", lookup_expr='lte')
    class Meta:
        model = Userpost
        field = '__all__'
        exclude = 'image', 'user', 'Price', 'Email', 'date_published'

