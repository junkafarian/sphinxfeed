sphinxfeed
==========

This Sphinx extension is derived from Dan Mackinlay's `sphinxcontrib.feed
<http://bitbucket.org/birkenfeld/sphinx-contrib/src/tip/feed/>`_ package.

It relies on the `feedformatter <http://code.google.com/p/feedformatter/>`_
package instead of Django utils to generate the feed.

Usage
-----

#. Install ``sphinxfeed`` using ``easy_install`` / ``pip`` /
   ``python setup.py install``

#. Add ``sphinxfeed`` to the list of extensions in your ``conf.py``::
   
       extensions = [..., 'sphinxfeed']

#. Customise the necessary configuration options to correctly generate the
   feed::

       feed_base_url = 'http://YOUR_HOST_URL'
       feed_author = 'YOUR NAME'

