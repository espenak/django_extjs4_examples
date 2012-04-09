from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "minimal_extjs4_app/index.django.html"
