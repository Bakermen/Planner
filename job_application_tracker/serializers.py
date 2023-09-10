from rest_framework.serializers import ModelSerializer

from .models import JobApplication


class JobApplicationSeralizer(ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"
