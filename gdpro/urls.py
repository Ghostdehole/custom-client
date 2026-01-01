import django
from uigdpro import views
from django.urls import path
from uigdpro import views as views
if django.__version__.split('.')[0]>='4':
    from django.urls import re_path as url
else:
    from django.conf.urls import  url, include

urlpatterns = [
    url(r'^$',views.generator_view),
    url(r'^generator',views.generator_view),
    url(r'^check_for_file',views.check_for_file),
    url(r'^download',views.download),
    url(r'^creategh',views.create_github_run),
    url(r'^updategh',views.update_github_run),
    url(r'^startgh',views.startgh),
    url(r'^get_png',views.get_png),
    url(r'^save_custom_client',views.save_custom_client),
    path('maintenance/', views.maintenance_view, name='maintenance')
]
