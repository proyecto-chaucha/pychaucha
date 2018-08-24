# -*- coding: utf-8 -*-
"""
Holds the Private key logic for Addresses
"""
import bitcoin

from chaucha import magicbytes
from .key import Key
from .public import Public


class Private(Key):

    def get_public(self):
        return Public(bitcoin.privtoaddr(self.key, magicbytes.default))

    @classmethod
    def init_random(cls: 'Private') -> 'Private':
        """
        Randomly creates a secure private key
        :return: Private key class object
        """
        key = bitcoin.sha256(
            bitcoin.sha256(
                bitcoin.random_key()
            )
        )
        return cls(key)

    @classmethod
    def init_from_seed(cls: 'Private', seed: str, once: bool=False) -> 'Private':
        """
        Creates a private key from a defined seed
        :param seed: string with the contents for key creation
        :param once: apply just one sha256 function (not recommended)
        :return: Private Key class object
        """
        key = bitcoin.sha256(
            bitcoin.sha256(
                seed
            )
        )

        if once:
            key = bitcoin.sha256(seed)

        return cls(key)
