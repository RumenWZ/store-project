from django.shortcuts import render

# Create your views here.
from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'index.html'

class ItemDetailsView(views.TemplateView):
    template_name = 'detail.html'