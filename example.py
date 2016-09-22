# coding: utf-8

from __future__ import print_function

from getenv import Env


app_name = 'FOO'

# Set the prefix for env vars
Env.set_prefix(app_name)

# Define your envs
ENV_PROCESSES = Env('{prefix}_PROCESSES', type=int, default=1)
ENV_DEBUG = Env('{prefix}_DEBUG', type=bool, default=False)
ENV_OPERATOR = Env('{prefix}_OPERATOR', default=None)


def main():
    processes = ENV_PROCESSES.get()
    debug = ENV_DEBUG.get()
    operator = ENV_OPERATOR.get()

    print('Run {} processes, debug = {}, operator = {}'.format(processes, debug, operator))


if __name__ == '__main__':
    main()
