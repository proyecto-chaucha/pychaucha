# -*- coding: utf-8 -*-


class Key(object):

    key = None

    def __init__(self, key: str):
        """
        Initialize using a unique string
        :param key: unique string representing a defined key
        """

        if key is None or key.strip() == '':
            raise ValueError('Key must not be empty')

        self.key = key

    def is_valid(self):
        raise NotImplementedError()
