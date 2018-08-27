from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import LookUp

from django.http import JsonResponse, HttpResponse
from django.core import serializers


@csrf_exempt
@require_http_methods(["GET", "POST"])
def url_lookup(request, **kwargs):
    if request.method == 'GET':
        domain = kwargs.get('domain', None)
        path = kwargs.get('path', None)
        if domain:
            if len(LookUp.objects.filter(url=domain)) > 0:
                return JsonResponse({'safe': False})
            elif len(LookUp.objects.filter(url=domain+"/"+str(path))) > 0:
                return JsonResponse({'safe': False})
            else:
                return JsonResponse({'safe': True})
        else:
            res = list(LookUp.objects.all().values())
            return JsonResponse(res, safe=False)

    if request.method == 'POST':
        domain = kwargs.get('domain', None)
        path = kwargs.get('path', '')
        if domain:
            res = LookUp.objects.create(url=domain+"/"+str(path))
            if res:
                return JsonResponse({'result': 'success'}, safe=False)
