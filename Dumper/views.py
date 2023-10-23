from django.shortcuts import render
from Dumper.models import Post, Comments
from django.views.generic import (TemplateView)

# Create your views here.

class AboutView(TemplateView):
    """ This view just mentions the purpose of the website """
    template_name = 'about.html'