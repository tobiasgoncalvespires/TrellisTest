from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    #path('', views.index, name='index'),
    path('num_to_english', views.TrellisView.as_view({'get': 'num_to_english', 'post': 'num_to_english'})),
    path('sera', views.TodoListApiView.as_view()),
])
