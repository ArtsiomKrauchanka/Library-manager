from django.contrib import admin
from django.conf import settings
from project import settings as media_settings
from django.conf.urls.static import static
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from landing import views as landing_views

admin.site.site_title = "Library Administration"
admin.site.site_header = "Library Administration"
admin.site.site_index = "Library "

urlpatterns = [
    path('admin_panel/', RedirectView.as_view(url=reverse_lazy('admin:index')), name='admin'),
    path('admin/', admin.site.urls),
    path('', landing_views.home, name='landing-home'),
    path('user/', include('users.urls')),
    path('', include('books.urls')),
    path('', include('ebooks.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(media_settings.MEDIA_URL, document_root=media_settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)