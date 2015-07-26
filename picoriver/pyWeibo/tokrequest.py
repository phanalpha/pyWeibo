"""Weibo OAuth 2.0 Requests, trade code for token.

.. moduleauthor:: Tsai Phan <phanalpha@hotmail.com>
"""

from urlrequest import URLRequest
from str_enum import StrEnum, value_of
from credential import Credential


class GrantType(StrEnum):
    AUTHORIZATION_CODE = 'authorization_code'


class AccessRequest(URLRequest):
    """Access request, trade authorization code for access token.
    """

    def __init__(self, app, redirect_uri, code):
        """Access request.
        """
        super(AccessRequest, self).__init__(
            'https://api.weibo.com/oauth2/access_token'
            '?client_id=YOUR_CLIENT_ID'
            '&client_secret=YOUR_CLIENT_SECRET'
            '&grant_type=authorization_code'
            '&redirect_uri=YOUR_REGISTERED_REDIRECT_URI'
            '&code=CODE'
        )

        self.app = app
        self.redirect_uri = redirect_uri
        self.code = code

    def build(self):
        return dict(
            client_id=self.app.id,
            client_secret=self.app.secret,
            grant_type=value_of(GrantType.AUTHORIZATION_CODE),
            redirect_uri=self.redirect_uri,
            code=self.code
        )

    def commit(self):
        """
        Returns:
            Credential.
        """
        res = super(AccessRequest, self).commit(True)

        return Credential(
            access_token=res['access_token'],
            expire_in=res['expires_in'],
            uid=res['uid']
        )
