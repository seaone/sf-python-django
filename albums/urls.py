from django.urls import path

from .views import AlbumList, AlbumDetail, PhotoList, PhotoDetail

urlpatterns = [
    path('photos/', PhotoList.as_view()),
    path('photos/<int:pk>/', PhotoDetail.as_view()),
    path('albums/', AlbumList.as_view()),
    path('albums/<int:pk>/', AlbumDetail.as_view()),
]
