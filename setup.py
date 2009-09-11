from setuptools import setup, find_packages
 
version = '0.1.0'
 
LONG_DESCRIPTION = """
=====================================
django-tagging-ext
=====================================
 
`django-tagging`_ gives you a lot of useful capabilities but it doesn't provide
 you with attractive views or synonym handling. This addresses those issues
  and more. 
"""
 
setup(
    name='django-tagging-ext',
    version=version,
    description="Adds in lots of features to supplement django-tagging",
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