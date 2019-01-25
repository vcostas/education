from django.views.generic import TemplateView
from django.urls import include, path
from app import settings
from app.views.LoginView import LoginView
from app.views.LogOutView import LogOutView
from app.views.ChangePasswordView import ChangePasswordView
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  # url(r'^api/', include('core.api.urls')),
                  # url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),

                  url(r'^index', TemplateView.as_view(template_name="index.html"), name='index'),

                  url(r'^$', LoginView.as_view(), name='login'),
                  url(r'^login/$', LoginView.as_view(), name='login'),
                  url(r'^accounts/login/$', LoginView.as_view(), name='login'),
                  url(r'^logout/', LogOutView.as_view(), name='logout'),
                  url(r'^change_password', ChangePasswordView.as_view(), name='change_password'),
                  url(r'^settings', TemplateView.as_view(template_name="settings.html"), name='settings'),

                  url('^', include('django.contrib.auth.urls')),
                  url(r'^reset_password/', PasswordResetView.as_view(template_name='registration/password_reset.html')),
                  url(r'^password_reset/done/$',
                      PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html')),
                  url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                      PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html')),
                  url(r'^reset/done/$',
                      PasswordResetCompleteView.as_view(template_name='registration/reset_done.html')),

                      # adding url path for correo app
                      path('correo/', include('correo.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
