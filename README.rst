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

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate djangocms_text_redactor


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


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
