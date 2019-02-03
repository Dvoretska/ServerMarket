from django.conf.urls import url
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView

from applications.accounts import views
from applications.accounts.views import UserVerifyJWT, ChangePasswordView

urlpatterns = [
    url(r'^signup/', RegisterView.as_view(), name='account_signup'),
    url(r'^login/', LoginView.as_view(), name='account_login'),
    url(r'^change-password/', ChangePasswordView.as_view(), name='change_password'),
    url(r'^api-token-verify/', UserVerifyJWT.as_view()),
    url(r'^profile/$', views.UserProfileView.as_view(), name='user_profile'),
    url(r'^destroy/$', views.UserProfileDestroyView.as_view(), name='destroy')
]
