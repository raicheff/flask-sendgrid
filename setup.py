#
# Flask-SendGrid
#
# Copyright (C) 2017 Boris Raicheff
# All rights reserved
#


from setuptools import setup


setup(
    name='Flask-SendGrid',
    version='0.1.0',
    description='Flask-SendGrid',
    author='Boris Raicheff',
    author_email='b@raicheff.com',
    url='https://github.com/raicheff/flask-sendgrid',
    install_requires=['flask', 'sendgrid', 'six'],
    py_modules=['flask_sendgrid'],
)


# EOF
