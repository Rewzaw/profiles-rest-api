from django.http import response
from rest_framework import status
from rest_framework.views import APIView, Response

from .serializers import HelloSerializer


class HelloApiVie(APIView):

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Just a get request that in this case returns an_apiview list below and a hello message"""

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

    def post(self, request):
        """Create a hello message to our name input"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            response = {'message': message}
            return Response(response)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating a specific object"""

        response = {'method': 'PUT'}
        return Response(response)

    def patch(self, request, pk=None):
        """Handle partial update of an object"""

        response = {'method': 'PATCH'}
        return Response(response)

    def delete(self, request, pk=None):
        """Handle deleting a specific object"""

        response = {'method': 'DELETE'}
        return Response(response)
