from django.contrib.auth import views as auth_views
from django.urls import path

from .views import bookmark_list, bookmark_user, bookmark_create, edit_bookmark

urlpatterns = [
    path('bookmarks/',
         bookmark_list,
         name='bookmark_list_view',
         ),
    path('bookmarks/create/',
         bookmark_create,
         name='bookmark_create_view',
         ),
    path('bookmarks/edit/<int:pk>',
         edit_bookmark,
         name='bookmark_edit_view',
         ),
    path('user/<str:username>/',
         bookmark_user,
         name='user_bookmark_view',
         ),
    path('login/',
         auth_views.LoginView.as_view(template_name='auth/login.html'),
         name='login',
         ),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='auth/logout.html'),
         name='logout'
         )
]
