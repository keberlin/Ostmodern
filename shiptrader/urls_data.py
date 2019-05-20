from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^starship$', StarshipView.as_view(), name='starship'),
    url(r'^starships$', StarshipsView.as_view(), name='starships'),
    url(r'^listing$', ListingView.as_view(), name='listing'),
    url(r'^listings$', ListingsView.as_view(), name='listings'),
    url(r'^activate$', ActivateView.as_view(), name='activate'),
    url(r'^deactivate$', DeactivateView.as_view(), name='deactivate'),
]