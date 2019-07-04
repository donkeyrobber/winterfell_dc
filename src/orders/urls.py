from django.urls import re_path, path

from . import views

urlpatterns = [
    path('order', views.index, name='order'),
    re_path(r'^order(?P<order_id>[0-9]+/$)', views.index, name='orders'),

]
