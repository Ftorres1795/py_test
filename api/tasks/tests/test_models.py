from django.test import TestCase

from ..models import Task

class TaskModelTest(TestCase):
    def test_valid_create_default(self):
        self.assertIsInstance(Task.objects.create(name='my task'),Task)
    
    def test_valid_create_status(self):
        self.assertIsInstance(
            Task.objects.create(name='my task', user= 80, status=2
        ),Task)

    def test_invalid_get_status(self):
        Task.objects.create(name='my task', status=3)
        self.assertTrue(isinstance(Task.objects.get(status=3),Task))