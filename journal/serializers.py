from rest_framework.serializers import ModelSerializer

from .models import Journal


class JournalSeralizer(ModelSerializer):
    class Meta:
        model = "Journal"
        fields = ["title", "date", "body"]


class SubJournalSeralizer(ModelSerializer):
    class Meta:
        model = "SubJournal"
        fields = ["titel", "image", "body"]
