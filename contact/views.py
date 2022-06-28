from django.views.generic import TemplateView


class PasswordContactView(TemplateView):
    template_name = 'contact/password_contact.html'
