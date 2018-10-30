from django.urls import path, re_path
from . import views

# path('', views.index, name='index'),

urlpatterns = [
   path('', views.HomePageView.as_view(), name='home'),
   path('about/', views.AboutPageView.as_view(), name='about'),
   path('country_areas', views.CountryAreaListView.as_view(), name='country_areas'),
   path('country_areas/<int:pk>', views.CountryAreaDetailView.as_view(), name='country_area_detail'),
   path('sites/', views.SiteListView.as_view(), name='sites'),
   path('sites/<int:pk>/', views.SiteDetailView.as_view(), name='site_detail'),
]
