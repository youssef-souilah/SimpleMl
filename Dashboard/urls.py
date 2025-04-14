from django.urls import path


from . import views

app_name="dashboard"
# path("<int:question_id>/results/", views.results, name="results"), for dynamic routes
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path('users/', views.user_list_view, name='users'),
    path('trains/', views.trains_view, name='trains'),
]