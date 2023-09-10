from django.shortcuts import render
from rest_framework import viewsets

from .models import Journal, SubJournals
from .serializers import JournalSeralizer, SubJournalSeralizer


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSeralizer


class SubJournalViewSet(viewsets.ModelViewSet):
    queryset = SubJournals.objects.all()
    serializer_class = SubJournalSeralizer
