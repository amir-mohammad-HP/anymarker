from django.urls import path, include, reverse_lazy
from authentification.views import EmailLoginView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path("login/", EmailLoginView.as_view(), name = 'login'),
    path("logout/", LogoutView.as_view(
        next_page = reverse_lazy("js_api_site:collection"),
    )),
]
