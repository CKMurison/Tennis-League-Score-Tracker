from rest_framework import serializers
from .models import *

class ReactSerializer(serializer.ModelSerializer):
    class meta:
        model = React
        fields = ['name', 'played', 'wins', 'draws', 'losses', 'games_for', 'games_against', 
                  'game_difference', 'total_points', 'form', 'bbb', 'wsb', 'tsb', 'bp', 'jvm']
    