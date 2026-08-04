from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.add_parcel, name='add_parcel'),
    path('track/', views.track, name='track'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("update-status/<int:id>/", views.update_status, name="update_status"),
    path("api/parcels/", views.parcel_api, name="parcel_api"),
]