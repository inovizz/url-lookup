"""Views for LookUp App."""

import json

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import JsonResponse
from django.core.cache import cache
from django.conf import settings

from .models import LookUp

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def url_lookup(request, **kwargs):
    """Url look up view for GET and POST methods.
        Arguments:
          request (HttpRequest): Reuest object
          kwargs(dict) : dictionary of keyword arguments
        Returns(JsonResponse): Response.
    """
    if request.method == 'GET':
        domain = kwargs.get('domain', "")
        path = kwargs.get('path', "")
        url = domain+"/"+path
        if url in cache:
            return JsonResponse({'result': 'URL is not safe to open.',
                                 'safe': False})
        if domain:
            if len(LookUp.objects.filter(url=url)) > 0:
                cache.set(url, True, timeout=CACHE_TTL)
                return JsonResponse({'result': 'URL is not safe to open.',
                                     'safe': False})
            return JsonResponse({'result': 'Not found in malware database, '
                                           'open it at your own risk!'})
        limit = int(request.GET.get('limit', 10))
        offset = int(request.GET.get('offset', 0))
        res = list(LookUp.objects.all()[offset: offset+limit].values())
        return JsonResponse({'result': res})

    if request.method == 'POST':
        data = request.body.decode('utf-8')
        url = json.loads(data)['url']
        if url:
            res = LookUp.objects.create(url=url)
            if res:
                return JsonResponse({'result': 'success'})
