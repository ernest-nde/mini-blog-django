from django.urls import path
from . import views

urlpatterns = [
    # POSTS
    # GET: /posts/
    path('', views.index, name='index'),

    # GET: /posts/<int:post_id>/
    path('<int:post_id>/', views.detail, name='detail'),

    # POST: /posts/create/
    path('create/', views.create, name='create'),

    # PUT: /posts/<int:post_id>/update/
    path('<int:post_id>/update/', views.update, name='update'),

    # DELETE: /posts/<int:post_id>/delete/
    path('<int:post_id>/delete/', views.delete, name='delete'),

    # COMMENTS 
    # GET: /posts/<int:post_id>/comments/
    path('<int:post_id>/comments/', views.list_comments, name='list_comments'),
    
    # POST: /posts/<int:post_id>/comments/
    path('<int:post_id>/comments/add/', views.add_comment, name='add_comment'),

    # GET: /posts/<int:post_id>/comments/<int:comment_id>/
    # path('<int:post_id>/comments/<int:comment_id>/', views.detail_comment, name='detail_comment'),

    # PUT: /posts/<int:post_id>/comments/<int:comment_id>/update/
    path('<int:post_id>/comments/<int:comment_id>/update/', views.update_comment, name='update_comment'),   

    # DELETE: /posts/<int:post_id>/comments/<int:comment_id>/delete/
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),   
]

