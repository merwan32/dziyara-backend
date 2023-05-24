from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='user-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('touristic-sites/', TouristicSiteListCreateView.as_view(), name='touristic-sites'),
    path('touristic-sites/by-name/', TouristicSiteByNameAPIView.as_view(), name='touristic-site-by-name'),
    path('comments/add/', UserCommentCreateView.as_view(), name='user-comment-create'),
]