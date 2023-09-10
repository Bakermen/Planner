from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# from django.views import View
# from django.views.generic.edit import UpdateView, DeleteView
# from django.views.generic import DetailView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import JobApplication
from .serializers import JobApplicationSeralizer


class JobApplicationViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly)
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSeralizer
