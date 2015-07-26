"""Resource requests.

.. moduleauthor:: Tsai Phan <phanalpha@hotmail.com>
"""

from urlrequest import URLRequest
from profile import Profile


class ProfileRequest(URLRequest):
    """Profile request.
    """

    def __init__(self, credential):
        super(ProfileRequest, self).__init__(
            'https://api.weibo.com/2/users/show.json'
            '?access_token=ACCESS_TOKEN'
            '&uid=UID'
        )

        self.credential = credential

    def build(self):
        return dict(
            access_token=self.credential.access_token,
            uid=self.credential.uid
        )

    def commit(self):
        """
        Returns:
            Profile.
        """
        res = super(ProfileRequest, self).commit()

        return Profile(
            id=res['id'],
            nickname=res['screen_name'],
            portrait=res['avatar_large'],
            gender=res['gender'],
            province=res['province'],
            city=res['city'],
            location=res['location'],
            description=res['description']
        )
