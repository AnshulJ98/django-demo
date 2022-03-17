from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    #/music/
    path('', views.IndexView.as_view(), name='index'),

    path('register/', views.UserFormView.as_view(), name='register'),

    #/music/<album_id>
    path('<str:pk>/', views.DetailView.as_view(), name="detail"),

    #/music/album/add
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    #/music/album/#/
    path('album/<str:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    #/music/album/#/delete/
    path('album/<str:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete')

]