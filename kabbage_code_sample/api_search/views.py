from django.views import generic
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect


class IndexView(generic.TemplateView):
    template_name = 'api_search/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated() == False:
            return redirect('/login/')
        else:
            return super(IndexView, self).get(request, *args, **kwargs)


class LoginView(generic.TemplateView):
    template_name = 'api_search/login.html'


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
