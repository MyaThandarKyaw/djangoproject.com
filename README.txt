This is the code that runs djangoproject.com, docs.djangoproject.com, and
(soon) code.djangoproject.com.

It's in the process of being cleaned up to make contribution easier; see
the TODO list, below.

However, it's ready for people to start contributing *now*; please feel
free to send pull requests and/or file tickets at code.djangoproject.com
with patches.

To run locally, do the usual::

    python manage.py runserver.

This runs as ``www.djangoproject.com``. To run locally as
``docs.djangoproject.com``, use::

    python manage.py runserver --settings=django_website.settings.docs
    
TODO:

    * Move all the Trac config into this repo.
    * Port all the code.djangoproject.com changes to work with Trac 0.12.
    * Deploying on the physical server is waiting on a server OS upgrade.