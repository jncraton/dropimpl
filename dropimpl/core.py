import ast


def strip_function_bodies(source_code, targets):
    '''
    removes the body of functions while preserving docstrings

    >>> code = "def add(a, b):\n    'adds things'\n    return a + b"
    >>> print(strip_function_bodies(code, ['add']))
    def add(a, b):
        'adds things'
        pass
    '''
    tree = ast.parse(source_code)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name in targets:
                docstring = ast.get_docstring(node)
                new_body = []
                if docstring:
                    new_body.append(ast.Expr(value=ast.Constant(value=docstring)))
                new_body.append(ast.Pass())
                node.body = new_body
    return ast.unparse(tree)


def generate_handout(input_file, output_file, targets):
    '''
    reads from input file and writes modified code to output file
    '''
    with open(input_file, 'r') as f:
        source = f.read()
    
    modified_code = strip_function_bodies(source, targets)
    
    with open(output_file, 'w') as f:
        f.write(modified_code)
