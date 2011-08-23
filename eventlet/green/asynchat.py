from eventlet import patcher
from eventlet.green import asyncore
from eventlet.green import socket

patcher.inject('asynchat',
    globals(),
    ('asyncore', asyncore),
    ('socket', socket))

del patcher