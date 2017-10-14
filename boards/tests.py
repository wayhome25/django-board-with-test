from django.test import TestCase
from django.urls.base import resolve
from django.urls.base import reverse

from boards.models import Board
from boards.views import board_topics
from boards.views import home


class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')  # return : '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')  # return : ResolverMatch(func=boards.views.home, args=(), kwargs={}, url_name=home, app_names=[], namespaces=[])
        self.assertEqual(view.func, home)


class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board <3')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)
