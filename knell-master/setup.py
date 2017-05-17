from setuptools import setup

setup(
    name='knell',
    packages=['knell'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'flask-sqlalchemy',
        'requests',
    ],
)
