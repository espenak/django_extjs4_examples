######################
Django extjs4 examples
######################

Example apps for `django_extjs4`_:

    generic_extjs4_app
        Uses the generic ``extjs4.views.Extjs4AppView`` to minimize the amount
        of Django-code required to create an extjs app.
    minimal_extjs4_app
        Exactly the same app as generic_extjs4_app, except that is defines its
        own view and template instead of using the generic one.  Great starting
        point for an extjs app that needs to define their own template. Note
        that a middle way between minimal_extjs4_app and generic_extjs4_app is
        to inherit from the ``extjs4/apptemplate.django.html`` template.



generic_extjs4_app explained
============================

Most Django ExtJS apps have really simple needs on the serverside:

- A template that checks if the server is in debug or production mode, and
  loads the appropriate ExtJS and app javascript.
- The ability to change ``<title></title>`` and the CSS path (for custom extjs
  themes).

The ``extjs4.views.Extjs4AppView`` class is a Django generic view that you just
add to your ``urls.py``. You can override:

    appname
        This is required. The view expects your ``app.js`` to be located in
        ``static/<appname>/``.
    title
        The ``<title></title>`` of the html document. Defaults
        to ``"ExtJS app"``.
    css_staticpath
        Staticfiles path to the CSS for the ExtJS theme. Defaults to
        ``"extjs4/resources/css/ext-all.css"``.
  
*Note:* We use ``settings.EXTJS4_DEBUG`` to separate between production and
development mode. See `django_extjs4`_ for information about EXTJS4_DEBUG.


minimal_extjs4_app explained
============================

All we really need to get a minimal extjs app up and running:

- a Django view like the one we have in ``minimal_extjs4_app/views.py`` with a template
like ``minimal_extjs4_app/templates/minimal_extjs4_app/index.django.html``.
- a normal extjs4 app like ``minimal_extjs4_app/static/minimal_extjs4_app/app.js``.
- specify appFolder in the ExtJS application (see ``app.js``).


Install minimal_extjs4_app or generic_extjs4_app
================================================

For this example we use ``minimal_extjs4_app``. The same instructions work for
``generic_extjs4_app``.

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
