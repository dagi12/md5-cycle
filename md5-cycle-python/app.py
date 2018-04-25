import binascii
import hashlib
import time


def current_timestamp():
    return int(round(time.time()))


def md5hash(plain):
    return hashlib.md5(hashlib.md5(plain).digest()).digest()[:7]


start = current_timestamp()

x0 = ""

tortoise = md5hash(x0)
hare = md5hash(md5hash(x0))

while tortoise != hare:
    tortoise = md5hash(tortoise)
    hare = md5hash(md5hash(hare))

tortoise = x0

while tortoise != hare:
    temp_tortoise = tortoise
    temp_hare = hare
    tortoise = md5hash(tortoise)
    hare = md5hash(hare)
    if tortoise == hare:
        print current_timestamp() - start
        print binascii.hexlify(temp_tortoise), binascii.hexlify(temp_hare)
