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


def test_type_not_supported():
    with assert_raises(TypeError):
        Env('A', type=object)


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


@with_setup(setup, teardown)
def test_type_float():
    with assert_raises(TypeError):
        Env('A', type=float, default=1)

    A = Env('A', type=float, default=1.1)

    assert_equal(A.get(), 1.1)

    setenv(A.key, '1.2')
    assert_equal(A.get(), 1.2)

    setenv(A.key, 'wtf')
    with assert_raises(ValueError):
        A.get()

    setenv(A.key, '12')
    v = A.get()
    assert_equal(v, 12.0)
    assert_equal(type(v), float)


@with_setup(setup, teardown)
def test_type_bool():
    with assert_raises(TypeError):
        Env('A', type=bool, default=0)

    A = Env('A', type=bool, default=True)

    assert A.get() is True, 'a = {}'.format(A.get())

    for i in A.bool_false_values:
        setenv(A.key, i)
        assert A.get() is False

    for i in A.bool_true_values:
        setenv(A.key, i)
        assert A.get() is True

    setenv(A.key, 'wtf')
    with assert_raises(ValueError):
        A.get()
