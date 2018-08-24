# -*- coding: utf-8 -*-
"""
Holds Public Key Logic
"""

from .key import Key


class Public(Key):

    def is_valid(self):
        # Should be more crypto accurate
        if len(self.key) == 34 and self.key[0] == 'c':
            return True

        return False
