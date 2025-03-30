from django.urls import path

from . import views

# path("<int:question_id>/results/", views.results, name="results"), for dynamic routes
urlpatterns = [
    path("", views.index, name="index"),
    path("app", views.app, name="app"),
    path("app/test", views.test, name="test"),
]