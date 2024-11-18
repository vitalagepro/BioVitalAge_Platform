from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main-page"),
    path("homepage/", views.HomePageView.as_view(), name="home_page"),
    path("calcolatore/", views.CalcolatoreView.as_view(), name="calcolatore"),
    path("risultati/", views.RisultatiView.as_view(), name="risultati"),
    path("persona/<int:id>/", views.PersonaDetailView.as_view(), name="persona_detail"),
]
