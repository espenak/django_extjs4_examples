######################
Django extjs4 examples
######################

Example apps for `django_extjs4`_. We only have one app, *minimal_extjs4_app*, at this time.


minimal_extjs4_app explained
============================

All we really need to get a minimal extjs app up and running:

- a Django view like the one we have in ``minimal_extjs4_app/views.py`` with a template
like ``minimal_extjs4_app/templates/minimal_extjs4_app/index.django.html``.
- a normal extjs4 app like ``minimal_extjs4_app/static/minimal_extjs4_app/app.js``.
- specify appFolder in the ExtJS application (see ``app.js``).


Install minimal_extjs4_app
--------------------------

1. Install `django_extjs4`_.
2. Copy ``minimal_extjs4_app/`` into your project and add it to ``INSTALLED_APPS``.
3. Add ``minimal_extjs4_app`` to your project urls::

    urlpatterns = patterns('',
                           ...
                           (r'^minimal_extjs4_app/', include('minimal_extjs4_app.urls')))
    ) + staticfiles_urlpatterns()



Deploy
======

See `djangosenchatools`_.


.. _`django_extjs4`: https://github.com/espenak/django_extjs4
.. _`djangosenchatools`: https://github.com/espenak/djangosenchatools
