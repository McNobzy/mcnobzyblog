from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('author/<str:pk>/<str:name>', views.postAuthor, name='postAuthor'),
    path('post/<str:pk>', views.viewPost, name='post'),
    path('edit/<str:pk>/', views.edit_post, name='edit'),
    path('search', views.search, name='search')
    # path('edit/<str:pk>/<str:func>', views.editPost, name="editPost")
]