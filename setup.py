from setuptools import setup

long_desc = '''
This package is derived from the feed Sphinx extension by Dan Mackinlay.

It creates an RSS feed of recently updated sphinx action.

It removes the original dependency on django.utils, replacing the functionality
with feedformatter
'''

requires = [
    'Sphinx>=0.6',
    'feedformatter',
    ]

setup(
    name='sphinxfeed',
    version='0.1',
    license='BSD',
    author='junkafarian',
    description='Sphinx extension for generating RSS feeds',
    long_description=long_desc,
    zip_safe=False,
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
