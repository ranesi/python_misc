from setuptools import setup

setup(
    name='Project4',
    version='0.02.dev',
    description='Vacation app',
    author='Group A',
    packages=[
        'Project4',
    ],
    install_requires=[
        'flask',
        'foursquare',
        'flask_sqlalchemy',
        'googlemaps',
    ],
)
