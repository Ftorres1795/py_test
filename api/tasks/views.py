from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import Task
from .serializers import TaskSerialiazer

class ListCreateTaskView(CreateModelMixin, ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialiazer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EditRetrieveTaskView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialiazer
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
