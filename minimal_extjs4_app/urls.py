from django.conf.urls.defaults import patterns, url

import views

urlpatterns = patterns('minimal_extjs4_app',
                       url(r'^$', views.IndexView.as_view()),
                      )
