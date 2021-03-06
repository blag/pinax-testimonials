from setuptools import find_packages, setup

VERSION = "2.0.5"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-testimonials.svg
    :target: https://pypi.python.org/pypi/pinax-testimonials/

==================
Pinax Testimonials
==================

.. image:: https://img.shields.io/pypi/v/pinax-testimonials.svg
    :target: https://pypi.python.org/pypi/pinax-testimonials/

\ 

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-testimonials.svg
    :target: https://circleci.com/gh/pinax/pinax-testimonials
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-testimonials.svg
    :target: https://codecov.io/gh/pinax/pinax-testimonials
.. image:: https://img.shields.io/github/contributors/pinax/pinax-testimonials.svg
    :target: https://github.com/pinax/pinax-testimonials/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-testimonials.svg
    :target: https://github.com/pinax/pinax-testimonials/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-testimonials.svg
    :target: https://github.com/pinax/pinax-testimonials/pulls?q=is%3Apr+is%3Aclosed

\ 

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT/

\ 

``pinax-testimonials`` is a well tested, documented, and proven solution for any site wanting to display testimonials.

Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+-----+
| Django / Python | 2.7 | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+=====+
| 1.11            |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
| 2.0             |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a testimonials app",
    name="pinax-testimonials",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-testimonials/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "testimonials": []
    },
    test_suite="runtests.runtests",
    tests_require=[
        "dj-inmemorystorage>=1.4.1",
        "django-appconf>=1.0.1",
        "django-test-plus>=1.0.22",
        "mock>=2.0.0",
        "django-user-accounts>=2.0.3",
    ],
    install_requires=[
        "django>=1.11",
        "django-appconf>=1.0.1"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)
