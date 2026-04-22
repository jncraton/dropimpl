# dropimpl

Generate student handout code by stripping function implementations while preserving docstrings.

## Usage

```sh
uvx dropimpl input.py output.py func1 func2
```

This writes output.py with the bodies of the named functions replaced by pass while keeping their docstrings.
