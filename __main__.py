#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Chaucha python tools
"""

from chaucha.address import Address

if __name__ == '__main__':
    address = Address.init_random()
    print('Private %s\nPublic %s' % (address.private.key, address.public.key))
