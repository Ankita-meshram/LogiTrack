from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.add_parcel, name='add_parcel'),
    path('track/', views.track, name='track'),
    path("login/", views.user_login, name="login"),
    path("signup/", views.signup, name="signup"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("update-status/<int:id>/", views.update_status, name="update_status"),
    path("api/parcels/", views.parcel_api, name="parcel_api"),
    path("admin-login/", views.admin_login, name="admin_login"),
    path("logout/", views.admin_logout, name="logout"),
    path("delete/<int:id>/",views.delete_parcel,name="delete_parcel"),
]