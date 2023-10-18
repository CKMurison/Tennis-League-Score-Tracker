from rest_framework import serializers
from .models import React

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['name', 'played', 'wins', 'draws', 'losses', 'games_for', 'games_against', 
                  'game_difference', 'total_points', 'form', 'bbb', 'wsb', 'tsb', 'bp', 'jvm']
    