from django.urls import path
from updates.views import *

app_name = 'updates'

urlpatterns = [
    path('', show_updates, name='updates'),
    path('post/', post_update, name='post_update'),
    path('get-updates', get_updates_json, name='get_updates_json'),
    path('get-updates-all', get_updates_json_all, name='get_updates_json_all'),
    path('delete/<int:pk>/', post_delete, name='post_delete'),
    path('json/', show_json, name='show_json'),
]