import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='face_frontalization',
    version='1.0',
    url='https://github.com/GrandathePanda/face-frontalization',

    author='Ian Butler',
    author_email='iantbutler01@gmail.com',
    description='Face frontalization library.',
    long_description=open('README.rst').read(),
    packages=['face_frontalization'],
    platforms='any',
    requires=['dlib', 'numpy', 'matplotlib'],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
