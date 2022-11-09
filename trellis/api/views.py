from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from requests import Response
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.request import Request


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
from rest_framework.views import APIView


class TrellisView(viewsets.ViewSet):

    def num_to_english(self, request: Request) -> HttpResponse:
        #request.data
        number = self.obter_parametro(request, 'number')
        if number is None:
            number = request.data['number']

        return HttpResponse('OK number is' + str(number), status=200)

    def obter_parametro(self, request: Request, nome: str, padrao=None):
        if nome in request.query_params:
            valor = request.query_params[nome]
            if valor is not None:
                return valor
        return padrao

class TodoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        return Response('OK 1.22', status=200)