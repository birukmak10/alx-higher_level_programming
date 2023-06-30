#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import urllib.request
from sys import argv


def request_id():
    """ displays the value of the X-Request-Id variable """
    with urllib.request.urlopen(argv[1]) as response:
        the_page = response.info()
    print(the_page['X-Request-Id'])


if __name__ == "__main__":
    request_id()
