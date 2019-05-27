from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Juegos
from .serializers import JuegosSerializer

# tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_juego(nombre="", descripcion="", empresa=""):
        if nombre != "" and descripcion != "" and empresa !="":
            Juegos.objects.create(nombre=nombre, descripcion=descripcion, empresa=empresa)

    def setUp(self):
        # add test data
        self.create_juego("DOOM", "Shooter rapido y frenetico", "id Software")
        self.create_juego("Quake Champions", "Multijugador arena rapido y frenetico", "id Software")
        self.create_juego("Rainbow Six: Siege", "Multijugador tactico", "Ubisoft")
        self.create_juego("The Witcher 3: Wild Hunt", "RPG mundo abierto", "CD Projekt")        

class GetAllJuegosTest(BaseViewTest):

    def test_get_all_juegos(self):
        """
        This test ensures that all juegos added in the setUp method
        exist when we make a GET request to the juegos/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("juegos-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Juegos.objects.all()
        serialized = JuegosSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)