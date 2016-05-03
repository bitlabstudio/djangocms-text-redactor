Important
=========

This app has been discontinued and is no longer maintained.

Django-cms Text Redactor
========================

A django-cms plugin that displays text and uses the
[Redactor](http://imperavi.com/redactor) editor for editing.

Note that Redactor requires a license, therefore it is not included in this
repository.


Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install djangocms-text-redactor

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/djangocms-text-redactor.git#egg=djangocms_text_redactor

Add ``djangocms_text_redactor`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'djangocms_text_redactor',
    )

Add the app's URLs to your ``urls.py``

.. code-block:: python

    urlpatterns += patterns(
        '',
        url(r'^djangocms-text-redactor/', include('djangocms_text_redactor.urls')),
        ...
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate djangocms_text_redactor

Make sure that you include the redactor CSS and JS files in the CMS template
that should contain the Redactor plugin.

Make sure to set the settings ``DJANGOCMS_TEXT_REDACTOR_IMAGE_UPLOAD_URL`` and
``DJANGOCMS_TEXT_REDACTOR_IMAGE_GET_JSON_URL`` to the url names of the two
views that handle this (see Redactor documentation).


Usage
-----

Add the ``Redactor plugin`` to one of your placeholders. It will have some
sane default settings. You can leave the settings for ``toolbarExternal``,
``imageUpload`` and ``imageGetJson`` as they are because they will be set
according to your settings.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 djangocms-text-redactor
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
