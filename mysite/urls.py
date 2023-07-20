from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from theme.views import change_theme
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('switch-theme', change_theme, name='change-theme'),
    path("__reload__/", include("django_browser_reload.urls")),
    # path('', include('tools.urls')),
    # path('account/', include('account.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]

urlpatterns += i18n_patterns (
    path('account/', include('account.urls')),
    path('', include('tools.urls')),
    path('admin/', admin.site.urls),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)