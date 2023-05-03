from rest_framework import serializers
from .models import Roster


class RosterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'position', 'depth', 'coach', 'created_at', 'updated_at')
        model = Roster