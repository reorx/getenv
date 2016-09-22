# getenv

Environment variable definition with type.

## Install

```bash
pip install getenv
```

## Usage

See `example.py`:

```python
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
```

Run `example.py` normally:

```bash
$ FOO_PROCESSES=3 python example.py
Run 3 processes, debug = False, operator = None
```

Then with envs:

```bash
$ FOO_PROCESSES=3 FOO_DEBUG=true FOO_OPERATOR=$(whoami) python example.py
Run 3 processes, debug = True, operator = reorx
```
