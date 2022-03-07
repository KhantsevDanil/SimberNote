from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.tag import TagViewSet
from api.views.note import NoteViewSet


app_name = "api"
router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('notes', NoteViewSet)


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
