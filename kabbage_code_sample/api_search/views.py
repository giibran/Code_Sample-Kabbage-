import requests
import json

from django.views import generic
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from allauth.socialaccount.models import SocialApp

from twython import Twython

SOCIAL_APP = SocialApp.objects.get(id=1)
APP_KEY = SOCIAL_APP.client_id
APP_SECRET = SOCIAL_APP.secret

APP_KEY = 'B4rAjU1kSMGVCC67BwQJIE3Yi'
APP_SECRET = 'KPmu2qVAhRpsk7PpDAjb9DlfTlwkfiEY2JLLJlZP80bddv73Uv'


class IndexView(generic.TemplateView):
    template_name = 'api_search/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated() is False:
            return redirect('/login/')
        else:
            return super(IndexView, self).get(request, *args, **kwargs)


class LoginView(generic.TemplateView):
    template_name = 'api_search/login.html'


class SearchView(APIView):

    def get(self, request, format=None):
        search_term = request.GET['search']
        service_used = request.GET['service']
        if service_used == 'wikipedia':
            wikipedia_url = 'https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch={search_term}+incategory:English-language_films'.format(search_term=search_term)  # noqa
            response = requests.get(wikipedia_url)
            response = json.loads(response.text)
        elif service_used == 'twitter':
            response = self.search_twitter(search_term)
        return Response(response)

    def search_twitter(self, search_term):
        twitter = Twython(APP_KEY, APP_SECRET)
        result_search = twitter.search(q=search_term, result_type='popular')
        return result_search


class LogoutRedirectView(generic.RedirectView):

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
            messages.add_message(
                request=request, level=messages.SUCCESS,
                message='Logout successful'
                )
        else:
            messages.add_message(
                request=request, level=messages.ERROR,
                message='There is no user logged in'
                )
        return super(LogoutRedirectView, self).get(request, *args, **kwargs)
