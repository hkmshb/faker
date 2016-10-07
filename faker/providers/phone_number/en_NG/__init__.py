from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '+234 ### ### ####',

        '070 #### ####',
        '080 #### ####',
        '081 #### ####',
        '090 2### ####',
        '090 3### ####',
        '090 5### ####',
        '090 8### ####',
        '090 9### ####',
        
        '01 ### ####',
        '0## ### ####',
    )
