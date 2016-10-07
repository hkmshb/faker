from __future__ import unicode_literals
from .. import Provider as InternetProvider



class Provider(InternetProvider):
    safe_email_tlds = ('com', 'net', 'org', 'ng')
    free_email_domains = ('gmail.com', 'yahoo.com', 'hotmail.com')
    tlds = ('com', 'com', 'com','net', 'org', 'ng', 'ng')
    