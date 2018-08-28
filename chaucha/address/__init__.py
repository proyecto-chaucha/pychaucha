# -*- coding: utf-8 -*-

from .private import Private


class Address(object):

    public = None
    private = None

    def __init__(self, _public: 'Public', _private: 'Private'):
        self.public = _public
        self.private = _private

    @classmethod
    def init_random(cls: 'Address') -> 'Address':
        """
        Randomly creates a secure private and public key
        :return: Address class object
        """
        _private = Private.init_random()
        _public = _private.get_public()
        return cls(_public, _private)

    @classmethod
    def init_from_seed(cls: 'Address', seed: str) -> 'Address':
        """
        Creates a private and public key from a defined seed
        :param seed: string with the contents for key creation
        :return: Address class object
        """
        _private = Private.init_from_seed(seed)
        _public = _private.get_public()
        return cls(_public, _private)

    @classmethod
    def init_from_seed_simple(cls: 'Address', seed: str) -> 'Address':
        """
        Creates a private and public key from a defined seed.
        Applies just one sha256 function to the seed (not recommended).
        :param seed: string with the contents for key creation
        :return: Address class object
        """
        _private = Private.init_from_seed_simple(seed)
        _public = _private.get_public()
        return cls(_public, _private)
