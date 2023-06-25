from django.urls import path
from .views import *

app_name = "jobs"

urlpatterns = [
    path("", ApplicationListView.as_view(), name="list"),
    path("application/<int:pk>", ApplicationDetailView.as_view(), name="application")
]
