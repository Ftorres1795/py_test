from django.test import TestCase

from ..serializers import TaskSerialiazer

class TaskSerializerTest(TestCase):
    def test_serializer_valid_data(self):
        data = {'name': 'my task', 'status': 2}
        serializer = TaskSerialiazer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_status(self):
        data = {'name': 'my task', 'status': 3}
        serializer = TaskSerialiazer(data=data)
        self.assertFalse(serializer.is_valid())