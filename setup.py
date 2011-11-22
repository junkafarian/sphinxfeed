from setuptools import setup

long_desc = open('README.rst').read()

requires = [
    'Sphinx>=0.6',
    'feedformatter',
    ]

setup(
    name='sphinxfeed',
    version='0.1',
    license='BSD',
    author='junkafarian',
    author_email='junkafarian@gmail.com',
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
