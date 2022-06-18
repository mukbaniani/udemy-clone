from django.urls import path
from . import views

urlpatterns = [
    path('add-teacher/', views.CreateTeacherView().as_view(), name='add-teacher'),
    path('update-teacher/<int:pk>', views.UpdateTeacherView().as_view(), name='update-teacher')
]
