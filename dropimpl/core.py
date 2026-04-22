import ast
import re


def strip_function_bodies(source_code, targets):
    """
    >>> code = "def add(a, b):\n    'adds things'\n    return a + b\n"
    >>> print(strip_function_bodies(code, ['add']))
    def add(a, b):
        'adds things'
        pass
    """
    tree = ast.parse(source_code)
    lines = source_code.splitlines(True)
    ops = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if node.name not in targets:
            continue
        body = node.body
        if not body:
            continue
        first_is_doc = (
            isinstance(body[0], ast.Expr)
            and isinstance(body[0].value, ast.Constant)
            and isinstance(body[0].value.value, str)
        )
        non_doc = body[1:] if first_is_doc else body
        if non_doc:
            first = non_doc[0]
            start = first.lineno - 1
            end = first.end_lineno - 1
            indent = (
                re.match(r"\s*", lines[start]).group(0)
                if start < len(lines)
                else "    "
            )
            ops.append((start, end, [indent + "pass\n"]))
            for stmt in non_doc[1:]:
                ops.append((stmt.lineno - 1, stmt.end_lineno - 1, []))
        else:
            doc = body[0]
            insert_at = doc.end_lineno
            idx = doc.end_lineno - 1
            indent = (
                re.match(r"\s*", lines[idx]).group(0) if idx < len(lines) else "    "
            )
            ops.append((insert_at, insert_at - 1, [indent + "pass\n"]))
    ops.sort(key=lambda x: x[0], reverse=True)
    for start, end, repl in ops:
        lines[start : end + 1] = repl
    return "".join(lines)


def generate_handout(input_file, output_file, targets):
    """
    reads from input file and writes modified code to output file
    """
    with open(input_file, "r") as f:
        source = f.read()
    modified_code = strip_function_bodies(source, targets)
    with open(output_file, "w") as f:
        f.write(modified_code)
