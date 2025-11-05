from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by("id")
    serializer_class = ItemSerializer


def home(request):
    text =(
        "This is the home page for Django for Ashley's Agriculture Management Software\n\n"
        "Frontend (React): http://localhost:5173/\n"
        "  -> npm install\n"
        "  -> npm run dev\n\n"
        "Backend (Django): http://127.0.0.1:8000/\n"
        "  -> python manage.py migrate\n"
        "  -> python manage.py runserver\n"
    )
    return HttpResponse (text, content_type="text/plain")
