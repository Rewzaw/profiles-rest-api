from django.http import response
from rest_framework.views import APIView, Response


class HelloApiVie(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a  traditional django view',
            'gives you the most control over the application logic',
            'is mapped manually to urls'
        ]

        response = {
            'message': 'Hello!',
            'an_apiview': an_apiview,
        }
        return Response(response)
