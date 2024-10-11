from django.urls import path

from . import views

#domain.com/meetings/...
#domain.com/meetings/1
#domain.com/meetings/rooms
#domain.com/meetings/new

urlpatterns=[
  path('detail/<int:id>',views.detail, name="detail"),

  path('rooms', views.rooms_list, name="rooms"),

  path('new', views.new, name="new"),
  path('', views.meetings_list_view, name='meetings'),  # List of meetings and rooms
]