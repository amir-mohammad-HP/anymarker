from django.urls import path
from api import views
from rest_framework import routers

app_name = 'calls'

urlpatterns = [
    # path(r'collection/', views.Get_Collection_List.as_view(), name = 'collection'),
]

# router = routers.DefaultRouter()
# router.register(r'collection', views.CollectionViewSet)
