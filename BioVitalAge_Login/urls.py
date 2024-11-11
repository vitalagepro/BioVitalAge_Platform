from django.urls import path
from django.urls import path, include



from . import views

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main-page"),
    path('HomePage', views.HomePageView.as_view(), name='home_page'),
    path('Calcolatore', views.CalcolatoreView.as_view(), name='calcolatore'),
    path('Risultati', views.RisultatiView.as_view(), name='risultati'),
    path('persona/<int:id>/', views.PersonaDetailView.as_view(), name='persona_detail'),
]