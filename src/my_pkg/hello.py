# -*- coding: utf-8 -*-
def _produce_message(name):
    return 'Hello {}'.format(name)


def say(name):
    print(_produce_message(name))
