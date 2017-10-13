from django.test import TestCase
from django.urls.base import resolve
from django.urls.base import reverse

from boards.views import home


class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')  # return : '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')  # return : ResolverMatch(func=boards.views.home, args=(), kwargs={}, url_name=home, app_names=[], namespaces=[])
        self.assertEqual(view.func, home)
