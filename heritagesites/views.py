from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import HeritageSite, CountryArea
from django.db.models import F

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the UNESCO Heritage Sites index page.")

class AboutPageView(generic.TemplateView):
    template_name = 'heritagesites/about.html'

class HomePageView(generic.TemplateView):
    template_name = 'heritagesites/home.html'

class SiteListView(generic.ListView):
    model = HeritageSite
    context_object_name = 'sites'
    template_name = 'heritagesites/site.html'
    paginate_by = 50

    def get_queryset(self):
        heritage_sites = HeritageSite.objects.all().select_related('heritage_site_category').order_by('site_name')
        return heritage_sites

class SiteDetailView(generic.DetailView):
    model = HeritageSite
    context_object_name = 'site'
    template_name = 'heritagesites/site_detail.html'

class CountryAreaListView(generic.ListView):
    model = CountryArea
    context_object_name = 'country_areas'
    template_name = 'heritagesites/country_area.html'
    paginate_by = 20

    def get_queryset(self):
        country_areas = CountryArea.objects.all().select_related('dev_status','location').order_by('country_area_name')
        return country_areas

class CountryAreaDetailView(generic.DetailView):
    model = CountryArea
    context_object_name = 'country_area'
    template_name = 'heritagesites/country_area_detail.html'
