"""Weibo open OAuth 2.0.

.. moduleauthor:: Tsai Phan <phanalpha@hotmail.com>
"""

import os
import base64

from authrequest import LoginRequest, Display, Language
from tokrequest import AccessRequest


class WbApp(object):
    """A open Weibo app identified by (App Key, App Secret).

    .. seealso:: <http://open.weibo.com/>
    """

    def __init__(self, appid, secret, redirect_uri):
        """App with key and secret.

        Args:
            appid (str): App Key
            secret (str): AppSecret
            redirect_uri (str):
        """
        self.id = appid
        self.secret = secret
        self.redirect_uri = redirect_uri

    def login(self, redirect_uri=None, state=None,
              display=Display.DEFAULT,
              language=Language.DEFAULT):
        """Initiate login authorization.

        The URLRequest could be committed in a client-side browser or so,
        in order to initiate the auth.

        Args:
            redirect_uri (str): uri to direct resource owner's user-agent back
                                after completing its interaction.

        Kwargs:
            state (str): an opaque value to maintain state
                         between the request and callback.

        Returns:
            A tuple with URLRequest, and the state.
        """
        if state is None:
            state = base64.urlsafe_b64encode(os.urandom(36))

        return LoginRequest(
            self,
            redirect_uri or self.redirect_uri,
            state,
            display,
            language
        ), state

    def access(self, code, redirect_uri = None):
        """Trade code for access token.

        Args:
            redirect_uri (str):
            code (str): authorization code.

        Returns:
            Credential, access token and openid or so.
        """
        return AccessRequest(self, redirect_uri or self.redirect_uri, code).commit()
