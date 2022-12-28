from rest_framework import serializers
from application.models import Weapon

# class WeaponSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=50)
#     strength = serializers.IntegerField()
#     protection = serializers.IntegerField()



class WeaponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weapon
        fields = ['title', 'strength', 'protection']
