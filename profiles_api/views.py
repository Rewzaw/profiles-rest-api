from django.http import response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Response

from . import models, permissions, serializers


class HelloApiView(APIView):
    """Test APIView"""

    serializer_class = serializers.HelloSerializer

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


class HelloViewSet(viewsets.ViewSet):
    """Test ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Just a get request that in this case returns a_viewset list below and a hello message"""

        a_viewset = [
            'uses Actions i.e (list, create, retreive, update, partial_update)',
            'automatically maps to urls using Routers',
            'provides more functionality with less code'
        ]

        response = {
            'message': 'Hello!',
            'a_viewset': a_viewset,
        }
        return Response(response)

    def retrieve(self, request, pk=None):
        """Handle getting specific object by ID"""

        response = {'method': 'GET'}
        return Response(response)

    def create(self, request):
        """Create a new hello message"""
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

    def update(self, request, pk=None):
        """Handle updating specific object"""

        response = {'method': 'PUT'}
        return Response(response)

    def partial_update(self, request, pk=None):
        """Handle partial update of an object"""

        response = {'method': 'PATCH'}
        return Response(response)

    def destroy(self, request, pk=None):
        """Handle deleting a specific object"""

        response = {'method': 'DELETE'}
        return Response(response)


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
