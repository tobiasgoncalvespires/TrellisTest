from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from trellis.api.views.number import NumberView

urlpatterns = format_suffix_patterns([
    path('num_to_english', NumberView.as_view({'get': 'num_to_english', 'post': 'num_to_english'}))
])
