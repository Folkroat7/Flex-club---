from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Sched, Booker
from .serialize import SchedSerializer, BookerSerializer
from django.shortcuts import render, redirect

class ScedListAPIView(generics.ListAPIView):
    queryset = Sched.objects.select_related('workout', 'trainer').all()
    serializer_class = SchedSerializer

class BookingCreateAPIView(generics.CreateAPIView):
    queryset = Booker.objects.all()
    serializer_class = BookerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class BookerDestroyAPIViev (generics.DestroyAPIView):
    permission_classes= permissions.IsAuthenticated

    def get_queryset(self):
        return Booker.objects.filter(user=self.request.user)
    
def mainPage (request):
    return render(request, 'main.html')

def schedPage(request):
    return render(request, 'page.html')

def contactsPage(request):
    return render(request, 'contacts.html')

def self(request):
    return render(request, 'self.html')
# Create your views here.
