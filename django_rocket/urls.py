from django.conf.urls import url
from django.contrib import admin

from .views import (
    InvitationCompletedView,
    InvitationView,
    RedeemInvitationView,
    RequestAccessCompletedView,
    RequestAccessView,
)

app_name = "django_rocket"

urlpatterns = [
    url(r'^$', InvitationView.as_view(),
        name='request_invitation'),
    url(r'^invitation_completed/$',
        InvitationCompletedView.as_view(),
        name='request_invitation_completed'),
    url(r'^request_access/$',
        RequestAccessView.as_view(),
        name='request_access'),
    url(r'^request_completed$',
        RequestAccessCompletedView.as_view(),
        name='request_access_completed'),
    url(r'^redeem_invitation/(?P<token>[a-f0-9]{40})/$',
        RedeemInvitationView.as_view(),
        name='redeem_invitation')
]
