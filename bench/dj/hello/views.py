import django
from django.http import HttpResponse

import random


def rand_string(min, max):
    """Returns a randomly-generated string, of a random length.

    Args:
        min (int): Minimum string length to return, inclusive
        max (int): Maximum string length to return, inclusive

    """

    int_gen = random.randint
    string_length = int_gen(min, max)
    return ''.join([chr(int_gen(ord(' '), ord('~')))
                    for __ in range(string_length)])

BODY = rand_string(10240, 10240).encode('utf-8') # NOQA
HEADERS = {'X-Test': 'Funky Chicken'}

_body = BODY
_headers = HEADERS


def hello(request, account_id):
    user_agent = request.META['HTTP_USER_AGENT']  # NOQA
    limit = request.GET.get('limit', '10')  # NOQA
    response = HttpResponse(_body)

    for name, value in _headers.items():
        response[name] = value

    return response
