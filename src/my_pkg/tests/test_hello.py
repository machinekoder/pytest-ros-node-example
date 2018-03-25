# -*- coding: utf-8 -*-
from my_pkg import hello


def test_hello_produces_friendly_message():
    message = hello._produce_message('Joe')

    assert message == 'Hello Joe'
