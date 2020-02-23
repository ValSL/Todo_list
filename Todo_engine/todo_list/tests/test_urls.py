from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todo_list.views import (
    index,
    TaskCreate,
    TaskUpdate,
    TaskDelete
)


class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('index_url')
        self.assertEqual(resolve(url).func, index)

    def test_create_url(self):
        url = reverse('create_url')
        self.assertEqual(resolve(url).func.view_class, TaskCreate)

    def test_update_url(self):
        url = reverse('update_url', args=[1])
        self.assertEqual(resolve(url).func.view_class, TaskUpdate)

    def test_delete_url(self):
        url = reverse('delete_url', args=[1])
        self.assertEqual(resolve(url).func.view_class, TaskDelete)
