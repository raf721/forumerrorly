"""Creates URL patterns for fe_app."""
from django.urls import path
from . import views

app_name = 'fe_app'

urlpatterns = [
    path('', views.index, name='index'),    # Home page
    path('threads/', views.threads, name='threads'),   # page showing all threads
    path('threads/<int:thread_id>/', views.thread, name='thread'),  # page for a single thread
    path('new_thread/', views.new_thread, name='new_thread'),   # page to add a new thread
    path('new_entry/<int:thread_id>/', views.new_post, name='new_post'),    # page to add new post to thread
]