from re import template
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class AchievementsPageView(TemplateView):
    template_name = 'achievements.html'

class TeamPageView(TemplateView):
    template_name = 'team.html'

class StrategiesPageView(TemplateView):
    template_name = 'strategies.html'