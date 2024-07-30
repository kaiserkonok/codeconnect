from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_answer/<int:question_id>/', views.post_answer, name='post_answer'),
]

