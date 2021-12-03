"""Creates URL patterns for fe_app."""
from django.urls import path
from . import views

app_name = 'fe_app'

urlpatterns = [
    path('', views.index, name='index'),    # Home page
    path('threads/', views.threads, name='threads'),   # page showing all threads
    path('threads/<int:thread_id>/', views.thread, name='thread'),  # page for a single thread
    path('new_thread/', views.new_thread, name='new_thread'),   # page to add a new thread
    path('thread/<int:post_id>/', views.post, name='post'),  # page for a single post   ???
    path('new_post/<int:thread_id>/', views.new_post, name='new_post'),    # page to add new post to thread
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),    # page to edit post
    path('new_comment/<int:post_id>/', views.new_comment, name='new_comment'),    # page to add comment
]