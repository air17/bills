from rest_framework.routers import SimpleRouter
from .views import BillViewSet

router = SimpleRouter()
router.register("bills", BillViewSet)

urlpatterns = router.urls
