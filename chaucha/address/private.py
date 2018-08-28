# -*- coding: utf-8 -*-
"""
Holds the Private key logic for Addresses
"""
import bitcoin

from chaucha import constants
from .key import Key
from .public import Public


class Private(Key):
    # TODO: Implement validation function to private keys
    def is_valid(self):
        pass

    def get_public(self):
        return Public(bitcoin.privtoaddr(self.key, constants.default))

    @classmethod
    def init_from_key(cls: 'Private', key: str) -> 'Private':
        """
        Creates a private key instance from already defined WIF key.
        Is the default init method.
        :param key: string with a WIF
        :return: Private Key class object
        """
        return cls(key)

    @classmethod
    def init_from_seed(cls: 'Private', seed: str) -> 'Private':
        """
        Creates a private key from a defined seed
        :param seed: string with the contents for key creation
        :return: Private Key class object
        """
        key = bitcoin.sha256(
            bitcoin.sha256(
                seed
            )
        )

        return cls(key)

    @classmethod
    def init_from_seed_simple(cls: 'Private', seed: str) -> 'Private':
        """
        Creates a private key from a defined seed.
        Applies just one sha256 function to the seed (Not recommended).
        :param seed: string with the contents for key creation
        :return: Private Key class object
        """
        key = bitcoin.sha256(seed)

        return cls(key)

    @classmethod
    def init_random(cls: 'Private') -> 'Private':
        """
        Randomly creates a secure private key
        :return: Private key class object
        """
        return cls.init_from_seed(bitcoin.random_key())
