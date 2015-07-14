import requests
import json
import wikipedia

from django.views import generic
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from allauth.socialaccount.models import SocialApp

from twython import Twython

try:
    SOCIAL_APP = SocialApp.objects.get(id=1)
    APP_KEY = SOCIAL_APP.client_id
    APP_SECRET = SOCIAL_APP.secret
except:
    ADMIN_NOT_SET = True


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
    try:
        if ADMIN_NOT_SET is True:
            pass
    except:
        def get(self, request, format=None):
            search_term = request.GET['search']
            service_used = request.GET['service']
            if service_used == 'wikipedia':
                wikipedia_search_term = "%20".join(search_term.split())
                try:
                    if request.GET['latitude']:
                        lat_lon = request.GET['latitude'] + "%7C" + request.GET['longitude']  # noqa
                        wikipedia_url = 'https://en.wikipedia.org/w/api.php?action=query&list=geosearch&format=json&gscoord={lat_lon}&gsradius=10000&gslimit=500'.format(search_term=wikipedia_search_term, lat_lon=lat_lon)  # noqa
                except:
                    wikipedia_url = 'https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch={search_term}'.format(search_term=wikipedia_search_term)  # noqa
                # wikipedia_url = 'https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch={search_term}'.format(search_term=wikipedia_search_term)  # noqa
                try:
                    if request.GET['latitude']:
                        response = requests.get(wikipedia_url)
                        response = json.loads(response.text)
                        filer_results = [
                            item
                            for item in response['query']['geosearch']
                            if search_term.lower() in item['title'].lower()
                            ]
                        response['query']['search'] = filer_results
                except:
                    response = requests.get(wikipedia_url)
                    response = json.loads(response.text)
            elif service_used == 'twitter':
                try:
                    if request.GET['latitude']:
                        geocode = '{latitude},{longitude},100mi'.format(
                            latitude=request.GET['latitude'],
                            longitude=request.GET['longitude']
                            )
                        response = self.search_twitter(search_term, geocode=geocode)  # noqa
                except:
                    response = self.search_twitter(search_term)
            return Response(response)

        def search_twitter(self, search_term, geocode=None):
            twitter = Twython(APP_KEY, APP_SECRET)
            if geocode:
                result_search = twitter.search(q=search_term, geocode=geocode)
            else:
                result_search = twitter.search(q=search_term)
            return result_search


class LogoutRedirectView(generic.RedirectView):

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(LogoutRedirectView, self).get(request, *args, **kwargs)
