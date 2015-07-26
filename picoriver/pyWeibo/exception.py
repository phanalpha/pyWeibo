"""Weibo errors, message and code.

.. moduleauthor:: Tsai Phan <phanalpha@hotmail.com>
"""

class WbException(Exception):
    """Weibo error.
    """

    def __init__(self, message, code):
        """Weibo error.

        Args:
            message (str): error message.
            code (int): error code.
        """
        super(WxException, self).__init__(message)

        self.code = code
