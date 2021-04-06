from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.index,name="Index"),
    path("review/review/<int:myid>/", views.view, name="Review"),
    path('review/review/', views.feedback, name="Feedback"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)