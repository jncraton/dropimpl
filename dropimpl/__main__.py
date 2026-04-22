import sys
from .core import generate_handout


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if len(argv) < 3:
        print("usage: dropimpl input.py output.py func1 func2")
        raise SystemExit(2)
    input_file = argv[0]
    output_file = argv[1]
    targets = argv[2:]
    generate_handout(input_file, output_file, targets)


if __name__ == "__main__":
    main()
