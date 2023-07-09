from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register('support_request', SupportRequestViewSet)

urlpatterns = router.urls

urlpatterns += [
]
