from http import HTTPStatus
from rest_framework.exceptions import APIException, PermissionDenied
import datetime
import logging

from django.conf import settings
from django.urls import path, re_path
from django.apps import apps
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponse
from django.utils.decorators import method_decorator

from django.views.decorators.cache import cache_page, cache_control, never_cache
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.csrf import csrf_exempt

from rest_framework import authentication, generics, parsers, renderers, status, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import api_view

import app.models as models
import app.serializers as serializers
import app.notifications as notifications

logger = logging.getLogger(__name__)


class NotYourProxy(APIException):
    status_code = 403
    default_detail = 'Member is not a proxy for current user.'
    default_code = 'forbidden'

class NotYourProxy(APIException):
    status_code = 403
    default_detail = 'Member is not a proxy for current user.'
    default_code = 'forbidden'

class MySubProxiesList(generics.ListAPIView):
    queryset = models.Member.objects.select_related('user')
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.MemberSerializer

    def get_queryset(self):
        return self.queryset.filter(proxy__user=self.request.user.id)


class MySuperProxiesList(generics.ListAPIView):
    queryset = models.Member.objects.select_related('user')
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.MemberSerializer

    def get_queryset(self):
        member = models.Member.objects.get(user=self.request.user.id)
        return self.queryset.filter(proxies=member.id)


class ProxyConnector(generics.GenericAPIView):
    '''connects members as proxies'''
    permission_classes = [IsAuthenticated]

    def put(self, request, proxy_id):
        try:
            proxy = models.Member.objects.get(id=proxy_id)
        except models.Member.DoesNotExist:
            return HttpResponseNotFound()

        # TOOD: Create proxy-request and have other user confirm first!
        #member = models.Member.get(user_id=self.request.user.id)
        # member.proxies.add(proxy)
        # member.save()
        # return HttpResponse("Created")

        return HttpResponseForbidden("Not yet implemented")

    def delete(self, request, proxy_id):
        try:
            proxy = models.Member.get(id=proxy_id)
        except models.Member.DoesNotExist:
            return HttpResponseNotFound()

        member = models.Member.get(user_id=self.request.user.id)
        member.proxies.remove(proxy)
        member.save()

        return HttpResponse("Deleted")


class ActivityByProxyEnlister(APIView):
    '''enlists on an activity via a proxy'''

    permission_classes = [IsAuthenticated]

    def get(self, request, activity_id, proxy_id):
        activity = models.Activity.objects.get(id=activity_id)
        proxy = models.Member.objects.get(id=proxy_id)
        master = models.Member.objects.get(user=self.request.user)

        return Response(
            data={'proxy_assigned': (
                activity.assigned == proxy and activity.assigned_for_proxy == master)}
        )

    def put(self, request, activity_id, proxy_id):
        proxy = models.Member.objects.get(id=proxy_id)
        master = models.Member.objects.get(user=self.request.user)

        if not master in proxy.proxy.all():
            raise NotYourProxy(
                f"Proxy {proxy} not registered to act on behalf of {master}.")

        activity = models.Activity.objects.select_related('event').get(id=activity_id)

        if activity.assigned is not None:
            raise PermissionDenied(
                f"Activity {activity} already assigned to someone.")

        if models.Activity.objects.filter(event=activity.event, assigned=proxy).exists():
            raise PermissionDenied(
                f"Proxy {proxy} already assigned to event {activity.event}.")

        logger.info(
            f"Assigning activity {activity} to {proxy} on behalf of {master}.")

        activity.assigned = proxy
        activity.assigned_for_proxy = master
        activity.assigned_at = datetime.datetime.now()
        activity.save()

        return Response(f"{proxy} is now assigned for {activity} on behalf of {master}.")

    def delete(self, request, activity_id, proxy_id):
        proxy = models.Member.objects.get(id=proxy_id)
        master = models.Member.objects.get(user=self.request.user)

        if not master in proxy.proxy.all():
            raise NotYourProxy(
                f"Proxy {proxy} not registered to act on behalf of {master}.")

        activity = models.Activity.objects.get(id=activity_id)

        if activity.assigned != proxy:
            raise PermissionDenied(f"Activity not assigned to proxy {proxy}.")

        if activity.assigned_for_proxy != master:
            raise PermissionDenied(f"Activity not assigned for for {master}.")

        logger.info(
            f"Delisting activity {activity} to {proxy} on behalf of {master}.")

        activity.assigned = None
        activity.assigned_for_proxy = None
        activity.assigned_at = None
        activity.save()

        return Response(f"{proxy} has been delisted from {activity} (was on behalf of {master})")


##############################################################################

url_patterns = [
    re_path(r'^proxy/(?P<proxy_id>[0-9]+)$', ProxyConnector.as_view()),
    re_path(r'^proxy/my/$', MySubProxiesList.as_view()),
    re_path(r'^proxy/my_super/$', MySuperProxiesList.as_view()),
    re_path(r'^proxy/activity/(?P<activity_id>[0-9]+)/(?P<proxy_id>[0-9]+)$',
            ActivityByProxyEnlister.as_view()),
]
