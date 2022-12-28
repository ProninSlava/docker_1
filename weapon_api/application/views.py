from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from application.models import Weapon
from application.serializers import WeaponSerializer


@api_view(['GET', 'POST'])
def weapon(request):
    if request.method == 'GET':
        weapons = Weapon.objects.all()
        weapon_api = WeaponSerializer(weapons, many=True)

        return Response(weapon_api.data)
        # return Response({'Оружие': WeaponSerializer(weapons, many=True).data})

    elif request.method == 'POST':
        weapon_new = Weapon.objects.create(title='БТР', strength=46, protection=23)

        return Response(f'Создан новый Weapon!')


class WeaponAPIview(APIView):
    def get(self, request):
        weapons = Weapon.objects.all()
        weapon_api = WeaponSerializer(weapons, many=True)

        template_name = 'application/weapon.html'
        context = {'weapons': weapon_api.data}
        return render(request, template_name, context)

         # return Response(weapon_api.data)

    def post(self, request):
        title = request.GET.get('title')
        strength = request.GET.get('strength')
        protection = request.GET.get('protection')
        weapon_new = Weapon.objects.create(title=title, strength=strength, protection=protection)

        return Response(f'Создан новый Weapon! {title} {strength} {protection}')

class WeaponListAPIView(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

class WeaponListCreateAPIView(ListCreateAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
