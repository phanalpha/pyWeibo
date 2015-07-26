"""User profile, nickname and portrait or so.

.. moduleauthor:: Tsai Phan <phanalpha@hotmail.com>
"""

from collections import namedtuple
from str_enum import StrEnum


class Gender(StrEnum):
    MALE = 'm'
    FEMALE = 'f'
    UNKNOWN = 'n'


class Profile(namedtuple('POProfile', [
        'id',
        'nickname',
        'portrait',
        'gender',
        'province',
        'city',
        'location',
        'description'
])):
    """User profile, nickname, portrait and more.
    """
