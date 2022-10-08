from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"), 
    path("edit", views.edit, name="edit"),
    path("save", views.save, name="save"),
    path("rand", views.rand, name="rand")
]
