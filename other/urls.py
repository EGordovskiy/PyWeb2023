from django.urls import path

from .views import CurrentDateView, IndexView
from store.views import CartView


urlpatterns = [
    path('', IndexView.as_view()),
    path('datetime/', CurrentDateView.as_view()),
    # path('hello/')
]

# localhost:8000/other/datetime