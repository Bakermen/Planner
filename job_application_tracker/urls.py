from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *


app_name = "jobs"

router = SimpleRouter()
router.register("jobapplication", JobApplicationViewSet, basename="job_application")

urlpatterns = router.urls
