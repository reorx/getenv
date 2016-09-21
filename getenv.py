# coding: utf-8

import os
import __builtin__


class Env(object):
    prefix = None
    _instances = {}
    supported_types = (str, int, bool, )

    def __init__(self, key,
                 type=str,
                 default=None,
                 allow_null=False):
        if self.prefix is None:
            raise ValueError('Please set prefix before using Env class')

        self.key = key.format(prefix=self.prefix)

        self.type = type
        type = __builtin__.type

        self.default = default
        if default is not None and not isinstance(default, self.type):
            raise TypeError(
                'default {} ({}) should be the same type of {}'.format(
                    default, type(default), self.type))

        self.allow_null = allow_null
        Env._instances[self.key] = self

    def get(self):
        v = os.environ.get(self.key, self.default)
        if not self.allow_null and not v:
            raise ValueError('No value for {} is not allowed'.format(self.key))
        return v

    @classmethod
    def set_prefix(cls, prefix):
        cls.prefix = prefix
