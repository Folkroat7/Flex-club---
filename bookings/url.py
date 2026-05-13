from django.urls import path
from .views import ScedListAPIView, BookingCreateAPIView, BookerDestroyAPIViev, mainPage, schedPage, contactsPage, self

urlpatterns = [
    path('api/sched/', ScedListAPIView.as_view(), name= 'sched-list'),
    path('api/book/', BookingCreateAPIView.as_view(), name = 'booking-create'),
    path('api/book/<int:pk>/', BookerDestroyAPIViev.as_view(), name = 'booker-delete'),
    path('', mainPage, name='new-page'),
    path('schedule/', schedPage, name = 'sched-page'),
    path('contacts/', contactsPage, name= 'contacts-page'),
    path('self/', self, name= 's')
]