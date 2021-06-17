# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages
 
setup(
    name='pip-facades-sample-python',
    version='1.0.0',
    url='https://github.com/pip-services-samples/pip-samples-facade-python',
    license='MIT',
    author='Conceptual Vision Consulting LLC',
    author_email='seroukhov@gmail.com',
    description='Sample Facade Microservice in Python',
    long_description=__doc__,
    packages=find_packages(exclude=['config', 'data', 'examples', 'test']),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=[
        'iso8601',
        'PyYAML',
        'pystache',
        'pytest',
        'pytz',
        'bottle',
        'requests',
        'cheroot',
        'beaker',
        'netifaces',
        'pip-services3-commons',
        'pip-services3-components',
        'pip-services3-container',
        'pip-services3-rpc',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]    
)