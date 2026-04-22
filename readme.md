# dropimpl

[![lint](https://github.com/jncraton/dropimpl/actions/workflows/lint.yml/badge.svg)](https://github.com/jncraton/dropimpl/actions/workflows/lint.yml) [![test](https://github.com/jncraton/dropimpl/actions/workflows/test.yml/badge.svg)](https://github.com/jncraton/dropimpl/actions/workflows/test.yml) [![deploy](https://github.com/jncraton/dropimpl/actions/workflows/deploy.yml/badge.svg)](https://github.com/jncraton/dropimpl/actions/workflows/deploy.yml) [![pypi](https://github.com/jncraton/dropimpl/actions/workflows/pypi.yml/badge.svg)](https://github.com/jncraton/dropimpl/actions/workflows/pypi.yml) [![release](https://github.com/jncraton/dropimpl/actions/workflows/release.yml/badge.svg)](https://github.com/jncraton/dropimpl/actions/workflows/release.yml)

Generate student handout code by stripping function implementations while preserving docstrings.

## Usage

```sh
uvx dropimpl input.py output.py func1 func2
```

This writes output.py with the bodies of the named functions replaced by pass while keeping their docstrings.
