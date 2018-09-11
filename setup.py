from setuptools import setup

requires = [
    'Sphinx>=0.6',
    'feedformatter',
    ]

# long_desc = open('README.rst').read()
long_desc = """ This Sphinx extension is a fork of Fergus Doyle's sphinxfeed
package which itself is derived from Dan Mackinlay's
`sphinxcontrib.feed
<http://bitbucket.org/birkenfeld/sphinx-contrib/src/tip/feed/>`_
package.  It relies on the `feedformatter
<http://code.google.com/p/feedformatter/>`_ package instead of Django
utils to generate the feed.

Features added by Luc:

- new config variable feed_field_name to change the name of the field
  to use for specifying the publication date.
- don't publish items whose publication datetime is in the future.

Usage
-----

#. Install ``sphinxfeed`` using ``easy_install`` / ``pip`` /
   ``python setup.py install``

#. Add ``sphinxfeed`` to the list of extensions in your ``conf.py``::
   
       extensions = [..., 'sphinxfeed']

#. Customise the necessary configuration options to correctly generate
   the feed::

       feed_base_url = 'http://YOUR_HOST_URL'
       feed_author = 'YOUR NAME'
       
       # optional options
       feed_description = "A longer description"
       feed_field_name = 'date'  # default value is "Publish Date"

"""

SETUP_INFO = dict(
    name='sphinxfeed',
    version='0.3',
    license='BSD',
    author='junkafarian',
    author_email='junkafarian@gmail.com',
    url='https://github.com/junkafarian/sphinxfeed',
    description='Sphinx extension for generating RSS feeds',
    long_description=long_desc,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    py_modules=['sphinxfeed'],
    include_package_data=True,
    install_requires=requires,
)


if __name__ == '__main__':
    setup(**SETUP_INFO)
