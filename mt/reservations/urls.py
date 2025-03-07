from django.urls import path
from .views import reservation_list, create_reservation

urlpatterns =[
    path('', reservation_list, name='reservation-list'),
    path('create/', create_reservation, name='create-reservation'),
]
