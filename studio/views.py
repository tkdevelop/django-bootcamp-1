from django.views.generic import TemplateView
 
class IndexView(TemplateView):
    template_name = "index.html"
 
class SupportView(TemplateView):
    template_name = "support.html"
 
class ContactView(TemplateView):
    template_name = "contact.html"