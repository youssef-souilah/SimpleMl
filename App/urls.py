from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name="app"
# path("<int:question_id>/results/", views.results, name="results"), for dynamic routes
urlpatterns = [
    path("", views.index, name="index"),
    path("app", views.app, name="app"),
    path("app/test", views.test, name="test"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)