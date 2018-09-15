from setuptools import setup

setup(
    name='News Headlines',
    version='1.0',
    py_modules=['news'],
    install_requires=[
        'Click', 'requests'
    ],
    entry_points='''
        [console_scripts]
        hello=news:cli,
    ''',
)