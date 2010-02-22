from setuptools import setup, find_packages
 
version = '0.2.0'
 
LONG_DESCRIPTION = """
=====================================
django-tagging-ext
=====================================
 
`django-tagging`_ gives you tagging. Django Tagging EXT gives you enhanced
displays of tags. It is `Django`_ neutral but when combined with `Pinax`_ 
gives you some extra view capabilities based off some of the Pinax core 
applications.

.. _`django-tagging`: http://code.google.com/p/django-tagging
.. _`Django`: http://djangoproject.com
"""
 
setup(
    name='django-tagging-ext',
    version=version,
    description="Adds in new features to supplement django-tagging",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='django,pinax',
    author='Daniel Greenfeld',
    author_email='pydanny@gmail.com',
    url='http://github.com/pydanny/django-tagging-ext/tree/master',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
    setup_requires=['setuptools_git'],
)