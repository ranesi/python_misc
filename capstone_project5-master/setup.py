from setuptools import setup

setup(
    name='mort',
    version='0.05.dev',
    description='CDC mortality data visualizer',
    author='ranesi',
    packages=[
        'mort',
    ],
    install_requires=[
        'flask',
        'sqlite3',
        'pygooglechart',
    ],
)
