from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Roster
from .serializer import RosterSerializer
from .permissions import isOwnerOrReadOnly

class RosterList(ListAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    queryset = Roster.objects.all()
    serializer_class = RosterSerializer

class RosterDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    queryset = Roster.objects.all()
    serializer_class = RosterSerializer