from setuptools import setup

setup(
    name='pycheckers',
    version='0.1',
    packages=['pycheckers', 'pycheckers.resources'],
    install_requires=['flask', 'flask-mysqldb', 'flask-sqlalchemy', 'flask-bcrypt', 'flask-login'],
    url='https://github.com/mciszczon/PyCheckers',
    license='MIT',
    author='mciszczon',
    author_email='contact@mciszczon.pl',
    description='English draughts web-based game in Flask'
)
