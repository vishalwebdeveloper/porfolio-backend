from django.shortcuts import render
from rest_framework import viewsets
from .models import Portfolio
from .serializers import PortfolioSerializer

# Create your views here.
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
