#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from setuptools import setup, find_packages
import os
import fancy_cronfield

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Framework :: Django',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.0',
    'Framework :: Django :: 2.1',
    'Framework :: Django :: 2.2',
]

INSTALL_REQUIREMENTS = [
    'django>=1.11,<3.0',
    'python-crontab==1.9.5',
]

readme_path = os.path.join(os.path.dirname(__file__), 'README.rst')
long_description = open(readme_path).read()

setup(
    name="django-fancy-cronfield-alt",
    author="Saeed Salehian",
    author_email="saeed.sq@gmail.com",
    maintainer='Ryan Siemens',
    maintainer_email='ryanjsiemens@gmail.com',
    version=fancy_cronfield.__version__,
    description="A nice and customizable cronfield",
    long_description=long_description,
    url='https://github.com/rsiemens/django-fancy-cronfield',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIREMENTS,
    extras_require={},
    packages=find_packages(exclude=[]),
    include_package_data=True,
    zip_safe=False,
    test_suite='runtests.main',
)
