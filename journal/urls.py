from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("journal", JournalViewSet, basename="journals")
router.register("sub-journal", SubJournalViewSet, basename="subjournals")

urlpatterns = router.urls
