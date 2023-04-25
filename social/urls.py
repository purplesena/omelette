from django.urls import path
from .views import ProfileEditView, ProfileView, People

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),
    path('people', People.as_view(), name='people'),
]