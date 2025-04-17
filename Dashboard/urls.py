from django.urls import path


from . import views

app_name="dashboard"
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path('users/', views.user_list_view, name='users'),
    path('trains/', views.trains_view, name='trains'),
    path('images/', views.images_usage_view, name='images'),
]