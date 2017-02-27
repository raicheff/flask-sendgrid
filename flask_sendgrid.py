#
# Flask-SendGrid
#
# Copyright (C) 2017 Boris Raicheff
# All rights reserved
#


import warnings

from flask import Response, request
from flask.signals import Namespace
from sendgrid import SendGridAPIClient
from six.moves.http_client import OK


sendgrid_events = Namespace().signal('sendgrid.events')


class SendGrid(object):
    """
    https://sendgrid.com/docs
    """

    client = None

    def __init__(self, app=None, blueprint=None):
        if app is not None:
            self.init_app(app, blueprint)

    def init_app(self, app, blueprint=None):

        api_key = app.config.get('SENDGRID_API_KEY')
        if api_key is None:
            warnings.warn('SENDGRID_API_KEY not set', RuntimeWarning, stacklevel=2)
            return

        self.client = SendGridAPIClient(apikey=api_key).client

        if blueprint is not None:
            blueprint.add_url_rule('/sendgrid', 'sendgrid', self.handle_webhook, methods=('POST',))

    def handle_webhook(self):
        """
        https://sendgrid.com/docs/API_Reference/Webhooks/
        """
        sendgrid_events.send(self, events_payload=request.get_json())
        return Response(status=OK)

    def __getattr__(self, name):
        return getattr(self.client, name)


# EOF
