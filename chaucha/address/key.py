# -*- coding: utf-8 -*-


class Key(object):

    key = None

    def __init__(self, key: str):

        if key is None or key.strip() == '':
            raise KeyError('Key must not be empty')

        self.key = key
