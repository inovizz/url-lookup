"""URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView

# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

# SCHEMA_VIEW = get_schema_view(title='codeXpose API',
#                               renderer_classes=[OpenAPIRenderer,
#                                                 SwaggerUIRenderer])

# using RedirectView to avoid impact on Json rendering
# print("&&&&&&&&&&&&&&&&&&", include('lookup.urls', 'lookup')[0].urlpatterns[0].url_patterns)
urlpatterns = [  # pylint: disable=invalid-name
    # path('', RedirectView.as_view(url="/lookup/")),
    path('admin/', admin.site.urls),
    path('', include('lookup.urls', 'lookup'))
    # path('api-token-auth/', obtain_jwt_token),
    # path('docs/', SCHEMA_VIEW),
    # path('api-auth/', include('rest_framework.urls',
    #                           namespace='rest_framework')),
]
