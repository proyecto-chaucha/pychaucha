#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Address helper functions
"""
import bitcoin
import chaucha.network as network


class Key(object):

    key = None

    def __init__(self, key: str):

        if key is None or key.strip() == '':
            raise KeyError('Key must not be empty')

        self.key = key


class Public(Key):

    def is_valid(self):
        # Should be more crypto accurate
        if len(self.key) == 34 and self.key[0] == 'c':
            return True

        return False


class Private(Key):

    def get_public(self):
        return Public(bitcoin.privtoaddr(self.key, network.magic))

    @classmethod
    def init_random(cls):
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
    def init_from_seed(cls, seed: str, once: bool = False):
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


class Address(object):

    public = None
    private = None

    def __init__(self, public: Public, private: Private):
        self.public = public
        self.private = private

    @classmethod
    def init_random(cls):
        """
        Randomly creates a secure private and public key
        :return: Address class object
        """
        private = Private.init_random()
        public = private.get_public()
        return cls(public, private)

    @classmethod
    def init_from_seed(cls, seed: str, once: bool = False):
        """
        Creates a private and public key from a defined seed
        :param seed: string with the contents for key creation
        :param once: apply just one sha256 function (not recommended)
        :return: Address class object
        """
        private = Private.init_from_seed(seed, once)
        public = private.get_public()
        return cls(public, private)
