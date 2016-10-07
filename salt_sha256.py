#salt+哈希算法
#这里先随机生成64bits的salt，再选择SHA-256算法使用HMAC对密码和salt进行10次叠代混淆，最后将salt和hash结果一起返回。

import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    if salt is None:
        salt = os.urandom(8) # 64 bits.

    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, unicode):
        password = password.encode('UTF-8')

    assert isinstance(password, str)

    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result
