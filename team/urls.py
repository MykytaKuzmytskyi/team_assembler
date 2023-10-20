from rest_framework.routers import DefaultRouter

from team.views import TeamViewSet

app_name = "team"

router = DefaultRouter()
router.register("team", TeamViewSet)
urlpatterns = router.urls
