from django.urls import path
from .views import PasswordContactView

app_name = 'contact'

urlpatterns = [
    path('', PasswordContactView.as_view(), name='password-contact'),
]
