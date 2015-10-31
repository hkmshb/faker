from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '070 #### ####',
        '080 #### ####',
        '081 #### ####',
        '090 #### ####',
    )
