from allauth.account.views import ConfirmEmailView
from django.conf.urls import url
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView

from applications.accounts import views
from applications.accounts.views import UserVerifyJWT

urlpatterns = [
    url(r'^signup', RegisterView.as_view(), name='account_signup'),
    url(r'^login', LoginView.as_view(), name='account_login'),
    url(r'^api-token-verify/', UserVerifyJWT.as_view()),
    url(r'^profile/$', views.UserProfileView.as_view(), name='user_profile'),
    url(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),
        name='account_confirm_email'),
]
