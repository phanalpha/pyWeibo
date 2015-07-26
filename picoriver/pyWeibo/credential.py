"""Access token, openid or so.

.. moduleauthor:: Tsai Phan <phanalpha@hotmail.com>
"""

from datetime import datetime, timedelta
from collections import namedtuple

from resrequest import ProfileRequest


class Credential(namedtuple('POCredential', [
        'access_token',
        'expire_at',
        'uid'
])):
    """Credential, access token and openid or so.
    """

    def __new__(cls, access_token, expire_in, uid):
        return super(Credential, cls).__new__(
            cls,
            access_token,
            datetime.utcnow() + timedelta(seconds=expire_in),
            uid
        )

    def profile(self):
        """User profile.

        Returns:
            Profile.

        Raises:
            WbException: access error, message and code.
        """
        return ProfileRequest(self).commit()
