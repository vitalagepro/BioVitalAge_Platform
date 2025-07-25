"""
DASHBOARD URLS configuration.
"""
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),
]