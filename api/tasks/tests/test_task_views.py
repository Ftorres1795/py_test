from django.test import TestCase, Client
from rest_framework import status
from ..models import Task

client = Client()

class TaskViewsTests(TestCase):

    def setUp(self) -> None:
        Task.objects.create(name='first task')
        Task.objects.create(name='second task')
        Task.objects.create(name='third task')

    def test_list_view(self):
        response = client.get('/api/tasks')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) == 3)

    def test_retrieve_view(self):
        response = client.get('/api/tasks/2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['name'] == 'second task')

    def test_create_view(self):
        response = client.post(
            '/api/tasks', 
            {'name': 'fourth task'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(isinstance(Task.objects.get(name='fourth task'), Task))

    def test_update_view(self):
        id = 1
        updatedName = 'my very first task'
        response = client.put(
            f'/api/tasks/{id}', 
            {'name': updatedName},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updatedTask = Task.objects.get(id=id)
        self.assertTrue(updatedTask.name == updatedName)

    def test_delete_view(self):
        id = 2
        response = client.delete(f'/api/tasks/{id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(Task.objects.filter(id=id).exists() == False)

