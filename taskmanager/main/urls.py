from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('<int:pk>/update', views.NoteUpdateView.as_view(), name='note-update'),
    path('<int:pk>/delete', views.NoteDeleteView.as_view(), name='note-delete'),
    path('register/', views.register, name='register')
]