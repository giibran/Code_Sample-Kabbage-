from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'api_search/index.html'
