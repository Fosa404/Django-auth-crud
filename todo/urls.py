from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="todo"),
    path('view/<int:id>/', views.view, name="view"),
    path('edit/<int:id>/', views.edit, name="todo_edit"),
    path('create/', views.create, name="todo_create"),
    path('delete/<int:id>/', views.delete, name="todo_delete"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)