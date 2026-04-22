import sys, os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from dropimpl.core import strip_function_bodies


def test_strip_basic():
    code = """def add(a, b):
    'adds things'
    return a + b
"""
    out = strip_function_bodies(code, ["add"])
    assert "pass" in out
    assert "adds things" in out


def test_docstring_indent():
    code = '''
def add(a, b):
    """ 
    Description

    Example:

    >>> add(1, 1)
    2
    """
    
    return a + b
'''
    out = strip_function_bodies(code, ["add"])
    assert out == code.replace("return a + b", "pass")
