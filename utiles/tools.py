import hashlib
from django.conf import settings


def hash_md5(info):
    info += settings.SECRET_KEY
    m = hashlib.md5()
    m.update(info.encode('utf8'))
    return m.hexdigest()
