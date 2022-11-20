from django.urls import path
from .views import HomePageView, AboutPageView, AchievementsPageView, TeamPageView, \
    StrategiesPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('achievements/', AchievementsPageView.as_view(), name='achievements'),
    path('team/', TeamPageView.as_view(), name='team'),
    path('strategies/', StrategiesPageView.as_view(), name='strategies'),
]