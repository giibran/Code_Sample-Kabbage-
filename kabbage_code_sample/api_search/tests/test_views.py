from django.test import TestCase
from django.contrib.auth.models import User
from api_search import views
from django.http.request import QueryDict


class TestApiSearch(TestCase):

    def create_test_user_profile(self):
        authentication_user = User.objects.create_user(
            username='test_username',
            password='test_password',
            email='test@test.com')
        return authentication_user

    def test_index_view_logged_in(self):
        self.create_test_user_profile()
        self.client.login(username='test_username', password='test_password',)
        response = self.client.get('/index/')
        self.assertTemplateUsed(
            response=response,
            template_name='api_search/index.html'
            )

    def test_index_view_not_logged_in(self):
        expected_url = '/login/'
        response = self.client.get('/index/')
        self.assertRedirects(
            response=response,
            expected_url=expected_url
            )

    def test_logout_view(self):
        status_code_expected = 200
        self.create_test_user_profile()
        self.client.login(username='test_username', password='test_password',)
        response = self.client.get('/accounts/logout/')
        self.assertEquals(
            response.status_code,
            status_code_expected)

    def test_search_view_with_wikipedia(self):
        status_code_expected = 200
        dictionary = {'search': 'guadalajara', 'service': 'wikipedia'}
        request = QueryDict('', mutable=True)
        request.GET = dictionary
        search_view = views.SearchView()
        response = search_view.get(request, format=None)
        self.assertEquals(
            response.status_code,
            status_code_expected
            )

    def test_search_view_with_twitter(self):
        status_code_expected = 200
        dictionary = {'search': 'guadalajara', 'service': 'twitter'}
        request = QueryDict('', mutable=True)
        request.GET = dictionary
        search_view = views.SearchView()
        response = search_view.get(request, format=None)
        self.assertEquals(
            response.status_code,
            status_code_expected
            )
