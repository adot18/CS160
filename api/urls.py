from django.urls import path
from .views import EventView

urlpatterns = [
    path('', EventView.as_view())
]