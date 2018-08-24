# -*- coding: utf-8 -*-

from .private import Private
from .public import Public


class Address(object):

    public = None
    private = None

    def __init__(self, _public: Public, _private: Private):
        self.public = _public
        self.private = _private

    @classmethod
    def init_random(cls: 'Address') -> 'Address':
        """
        Randomly creates a secure private and public key
        :return: Address class object
        """
        private = Private.init_random()
        public = private.get_public()
        return cls(public, private)

    @classmethod
    def init_from_seed(cls: 'Address', seed: str, once: bool=False) -> 'Address':
        """
        Creates a private and public key from a defined seed
        :param seed: string with the contents for key creation
        :param once: apply just one sha256 function (not recommended)
        :return: Address class object
        """
        private = Private.init_from_seed(seed, once)
        public = private.get_public()
        return cls(public, private)
