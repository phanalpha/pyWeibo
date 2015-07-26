"""URLRequest, Weixin request common ops.

.. moduleauthor:: Tsai Phan <phanalpha@hotmail.com>
"""

from urllib import urlencode
from urlparse import urlparse, urlunparse, ParseResult
from contextlib import closing
from exception import WbException

import urllib2
import json


class URLRequest(object):
    """URLRequest, common ops.
    """

    def __init__(self, url):
        """URLRequest.

        Args:
            url (str): url sample.
        """
        self.url = isinstance(url, ParseResult) and url or urlparse(url)

    def query(self, **kwargs):
        """New request with query.

        Returns:
            New URLRequest.
        """
        return URLRequest(ParseResult(
            self.url.scheme,
            self.url.netloc,
            self.url.path,
            self.url.params,
            urlencode(kwargs),
            self.url.fragment
        ))

    def __str__(self):
        return urlunparse(self.url)

    def build(self):
        pass

    def commit(self, post=False):
        """Commit request.

        Returns:
            JSON / dict.

        Raises:
            WbException: Weibo error message and code.
        """
        with closing(
                post and
                urllib2.urlopen(str(self.query()), urlencode(self.build())) or
                urllib2.urlopen(str(self.query(**self.build())))
        ) as f:
            res = json.load(f)

        if res.get('error'):
            raise WbException(res['error_description'], res['error_code'])

        return res
