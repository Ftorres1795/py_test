from django.urls import path

from .views import ListCreateTaskView, EditRetrieveTaskView

urlpatterns = [path('tasks', ListCreateTaskView.as_view()),
               path('tasks/<int:pk>', EditRetrieveTaskView.as_view())]