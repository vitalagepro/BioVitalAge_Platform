"""
URLS ROOT mappings configuration
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    path('admin/',  admin.site.urls),

    # Schema JSON/YAML
    path("api/schema/", SpectacularAPIView.as_view(), name="schema" ),

    # SWAGGER UI
    path("api/docs/", SpectacularSwaggerView.as_view(url_name='schema'), name="swagger-ui"),

    # REDOC
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # API
    path('api/', include("api.urls")),

    # DASHBOARD
    path("", include("Dashboard.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
