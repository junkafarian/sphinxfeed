from distutils.core import setup

long_desc = open('README.rst').read()

requires = [
    'Sphinx>=0.6',
    'feedformatter',
    ]

setup(
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
