# coding: utf-8
# flake8: N806

import os
from nose.tools import with_setup, assert_equal, assert_raises
from getenv import Env

store = {}


def setup():
    store['old_environ'] = dict(os.environ)


def teardown():
    os.environ.clear()
    os.environ.update(store['old_environ'])


def setenv(k, v):
    os.environ[k] = v


@with_setup(setup, teardown)
def test_basic():
    # because prefix is not set
    with assert_raises(ValueError):
        Env('{prefix}_A')

    Env.set_prefix('FOO')
    A = Env('{prefix}_A')

    assert_equal(A.key, 'FOO_A')

    # because of allow_null=False
    with assert_raises(ValueError):
        A.get()

    v = 'bar'
    setenv(A.key, v)
    assert_equal(A.get(), v)


@with_setup(setup, teardown)
def test_allow_null():
    A = Env('A', allow_null=True)
    assert A.get() is None


@with_setup(setup, teardown)
def test_default():
    # because 1 is not of type str
    with assert_raises(TypeError):
        Env('A', default=1)

    default = 'qur'
    A = Env('A', default=default)
    assert_equal(A.get(), default)


@with_setup(setup, teardown)
def test_type_int():
    A = Env('A', type=int, default=1)

    assert_equal(A.get(), 1)

    setenv(A.key, '12')
    assert_equal(A.get(), 12)

    setenv(A.key, 'wtf')
    with assert_raises(ValueError):
        A.get()

    setenv(A.key, '1.2')
    with assert_raises(ValueError):
        A.get()
