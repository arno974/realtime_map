from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView 

urlpatterns = patterns('websockets_map',
    
    (r"^$", TemplateView.as_view(template_name='index.html')),
)
