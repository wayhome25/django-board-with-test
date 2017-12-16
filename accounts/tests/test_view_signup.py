from django.contrib.auth.models import User
from django.test import TestCase
from django.urls.base import resolve
from django.urls.base import reverse

from accounts.forms import SignUpForm
from accounts.views import signup


class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')  # 실제 url으로 부터 연결되는 view function 관련 정보를 담은 ResolverMatch 객체를 리턴
        self.assertEqual(view.func, signup)
        self.assertEqual(view.view_name, 'signup')

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)

    def test_form_inputs(self):
        """The view must contain six inputs: csrf, username, email, password1, password2, submit button"""
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)


class SuccessfulSignUpTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email': 'test@abc.com',
            'password1': 'asdf1234',
            'password2': 'asdf1234'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_회원가입_성공후_리다이랙트(self):
        self.assertRedirects(self.response, self.home_url)

    def test_회원가입_성공후_유저레코드생성(self):
        self.assertTrue(User.objects.exists())

    def test_회원가입_성공후_유저로그인(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignUpTestCase(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})

    def test_signup_status_code(self):
        """invalid form submission should return to the same page"""
        self.assertEqual(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')

        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())
