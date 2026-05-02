from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from donations.views import (
    DonationViewSet,
    home,
    manage_requests,
    accept_request,
    reject_request
)
from users.views import (
    register_view,
    login_view,
    logout_view
)
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
router.register(r'donations', DonationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home),
    path('manage-requests/',manage_requests),
    path('accept-request/<int:id>/',accept_request),
    path('reject-request/<int:id>/',reject_request),
    path('register/',register_view),
    path('login/',login_view),
    path('logout/',logout_view),
]

urlpatterns+=static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)