from django.urls import path


from . import views

app_name="dashboard"
# path("<int:question_id>/results/", views.results, name="results"), for dynamic routes
urlpatterns = [
    path("", views.dashboard, name="dashboard")
]