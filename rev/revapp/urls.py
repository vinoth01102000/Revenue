from revapp import views
from django.urls import path


urlpatterns = [
    path('registered/', views.RegisterAPIView.as_view(),name="registered")
]