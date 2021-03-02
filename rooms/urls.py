from rest_framework.routers import DefaultRouter
from django.urls import path
from . import viewsets

router = DefaultRouter()
router.register('', viewsets.RoomViewSet, basename="room")

app_name = "rooms"

urlpatterns = router.urls
