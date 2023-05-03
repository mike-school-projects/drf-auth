from django.urls import path
from .views import RosterList, RosterDetail

urlpatterns = [
    path('', RosterList.as_view(), name='roster_list'),
    path('<int:pk>', RosterDetail.as_view(), name='roster_detail'),
]