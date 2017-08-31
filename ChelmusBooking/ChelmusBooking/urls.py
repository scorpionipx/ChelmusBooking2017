from django.conf.urls import url
from django.contrib import admin

from .views import HomePageView
from .views import SignUpView
from .views import LoginView

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url('^$', HomePageView.as_view(), name='home'),
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
]
