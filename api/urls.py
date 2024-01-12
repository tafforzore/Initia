from django.urls import path,include
from api import views

urlpatterns = [
    path('notify/', views.NotifyAPIView.as_view(), name='notify'),
    path('cancel/', views.apiMessage.cancel, name='notify'),
    path('success/', views.apiMessage.success, name='notify'),
]