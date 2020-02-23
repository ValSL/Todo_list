from django.test import TestCase, Client
from django.urls import reverse
from todo_list.models import Task
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('index_url')
        self.task = Task.objects.create(title='test', content='test', priority='red')
        self.detail_url = reverse('detail_url', args=[1])
        self.delete_url = reverse('delete_url', kwargs={'pk': self.task.id})
        self.update_url = reverse('update_url', kwargs={'pk': self.task.id})

    def test_todo_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_list/index.html')

    def test_todo_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_list/detail.html')

    def test_todo_create_POST(self):
        url = reverse('create_url')

        response = self.client.post(url, {
            'title': 'test2',
            'content': 'test2',
            'priority': 'green'
        })

        task2 = Task.objects.get(pk=2)

        self.assertEquals(task2.title, 'test2')
        self.assertEquals(task2.content, 'test2')
        self.assertEquals(task2.priority, 'green')

    def test_todo_delete_POST(self):
        response = self.client.delete(self.delete_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Task.objects.all().count(), 0)

    def test_todo_update_POST(self):
        response = self.client.post(self.update_url, {
            'title': 'new',
            'content': 'new',
            'priority': 'green'
        })

        self.task.refresh_from_db()
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.task.title, 'new')
