from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.user_profile),
    path('profile/<int:user_pk>/follow/', views.follow)
]