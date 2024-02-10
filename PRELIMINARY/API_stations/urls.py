from django.urls import path
from .views import *

urlpatterns = [
    path('', StationListView.as_view()), # api/stations
    # path('/<int:id>/trains', StationTrainsView.as_view()), # api/stations/{station_id}/trains
]
