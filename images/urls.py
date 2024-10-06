from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('download/<int:image_id>/', views.download_image, name='download_image'),
    path('api/random/', views.random_image, name='random_image'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
