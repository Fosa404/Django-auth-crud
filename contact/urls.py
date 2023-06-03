from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="contact"),
    path('<letter>', views.index, name="contact"),
    path('view/<int:id>', views.view, name="contact_view"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('create/', views.create, name="create"),
    path('delete/<int:id>', views.delete, name="delete")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)