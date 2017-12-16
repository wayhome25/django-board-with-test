from django.test import TestCase

from accounts.forms import SignUpForm


class SignUpFormTest(TestCase):
    def test_회원가입폼_필드확인(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2']
        actual = list(form.fields)
        self.assertEqual(expected, actual)
