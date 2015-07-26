"""Weibo OAuth 2.0 Requests, initiate login authorization.

.. moduleauthor:: Tsai Phan <phanalpha@hotmail.com>
"""

from urlrequest import URLRequest
from str_enum import StrEnum, value_of


class Display(StrEnum):
    """Authorization endpoints.
    """

    DEFAULT = 'default'         # web
    MOBILE = 'mobile'           # html5, mobile
    WAP = 'wap'                 # wap, mobile
    CLIENT = 'client'           # pc or so
    APPON = 'apponweibo'        # in site


class Scope(StrEnum):
    """Scope options.
    """

    ALL = 'all'
    EMAIL = 'email'
    DIRECT_MESSAGES_WRITE = 'direct_messages_write'
    DIRECT_MESSAGES_READ = 'direct_messages_read'
    INVITATION_WRITE = 'invitation_write'
    FRIENDSHIPS_GROUPS_READ = 'friendships_groups_read'
    FRIENDSHIPS_GROUPS_WRITE = 'friendships_groups_write'
    STATUSES_TO_ME_READ = 'statuses_to_me_read'
    FOLLOW_APP_OFFICIAL_MICROBLOG = 'follow_app_official_microblog'


class Language(StrEnum):
    """Language options.
    """

    DEFAULT = ''
    ENGLISH = 'en'


class AuthRequest(URLRequest):
    """Authorization requests, a base class.
    """

    def __init__(self, app, redirect_uri,
                 scopes=[],
                 state=None,
                 display=Display.DEFAULT,
                 force_login=False,
                 language=Language.DEFAULT):
        """Authorization requests.
        """
        super(AuthRequest, self).__init__(
            'https://api.weibo.com/oauth2/authorize'
            '?client_id=YOUR_CLIENT_ID'
            '&response_type=code'
            '&redirect_uri=YOUR_REGISTERED_REDIRECT_URI'
        )

        self.app = app
        self.redirect_uri = redirect_uri
        self.scopes = scopes
        self.state = state
        self.display = display
        self.force_login = force_login
        self.language = language

    def __str__(self):
        return str(self.query(
            client_id=self.app.id,
            redirect_uri=self.redirect_uri,
            scope=','.join(map(value_of, self.scopes)),
            state=self.state or '',
            display=value_of(self.display),
            forcelogin=str(self.force_login).lower(),
            language=value_of(self.language)
        ))


class LoginRequest(AuthRequest):
    """Weibo login authorization request.
    """

    def __init__(self, app, redirect_uri, state,
                 display=Display.DEFAULT,
                 language=Language.DEFAULT):
        """Weibo login.

        .. see also:: AuthRequest
        """
        super(LoginRequest, self).__init__(
            app,
            redirect_uri,
            state=state,
            display=display,
            language=language
        )
