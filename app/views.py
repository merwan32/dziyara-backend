from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework import generics
from .serializer import *
from rest_framework.permissions import IsAuthenticated



from rest_framework_simplejwt.tokens import RefreshToken

class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            UserProfile.objects.create(user=user, phone_number=serializer.validated_data['phone_number'])

            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token

            return Response(
                {'message': 'User created successfully.', 'access_token': str(access_token), 'refresh_token': str(refresh_token)},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=400)

        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token

        return Response({'access_token': str(access_token), 'refresh_token': str(refresh_token)})





class TouristicSiteListCreateView(generics.ListCreateAPIView):
    queryset = TouristicSite.objects.all()
    serializer_class = TouristicMapSiteSerializer

class TouristicSiteByNameAPIView(APIView):
    def get(self, request):
        site_name = request.query_params.get('name', None)
        if site_name:
            try:
                site = TouristicSite.objects.get(site_name=site_name)
                serializer = TouristicSiteSerializer(site)
                return Response(serializer.data)
            except TouristicSite.DoesNotExist:
                return Response({'error': 'Touristic site not found.'}, status=404)
        else:
            return Response({'error': 'Missing "name" parameter.'}, status=400)


class UserCommentCreateView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # Access the authenticated user
        serializer = UserCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)