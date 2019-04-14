from lark import Lark
from lark.indenter import Indenter
from lark.lexer import Token
from lark.tree import Tree


class PythonIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8

kwargs = dict(rel_to=__file__, postlex=PythonIndenter(), start='file_input')

python_parser3 = Lark.open('python3.lark', parser='lalr', **kwargs)


class StackFrame(object):
    """Stack frame class."""
    def __init__(self):
        self.frame_locals = {}

    def dump(self):
        """Dump the stack."""
        print("========= Stack Locals ==========")
        print(self.frame_locals)


class Var(object):
    """Variable class."""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

# TODO - Make builtin types, including int, float, and object.
# TOOD - Implement base object functions to perform arithmetic: https://docs.python.org/3.7/reference/datamodel.html#emulating-numeric-types


# Global stack frame
global_frame = StackFrame()

def run_instruction(t):
    if t.data == 'expr_stmt':
        var_name = t.children[0].children[0].value
        result = run_instruction(t.children[1])
        global_frame.frame_locals[var_name] = Var(result)
    elif t.data == 'arith_expr' or t.data == 'term':
        result = None
        next_operand = None
        for child in t.children:
            if isinstance(child, Tree):
                if child.data == "term":
                    x = run_instruction(child)
                    if result is None:
                        result = x
                    elif result is not None:
                        if next_operand.type == "PLUS":
                            result = result + x
                        elif next_operand.type == "MINUS":
                            result = result - x
                        elif next_operand.type == "STAR":
                            result = result * x
                        elif next_operand.type == "SLASH":
                            result = result / x

                if child.data == "number":
                    x = int(child.children[0].value)
                    if result is None:
                        result = x
                    elif result is not None:
                        if next_operand.type == "PLUS":
                            result = result + x
                        elif next_operand.type == "MINUS":
                            result = result - x
                        elif next_operand.type == "STAR":
                            result = result * x
                        elif next_operand.type == "SLASH":
                            result = result / x
            elif isinstance(child, Token):
                next_operand = child
        return result
    else:
        raise SyntaxError('Unknown instruction: %s' % t.data)


def main():
    ENABLE_TIMING = True

    from timeit import default_timer as timer

    if ENABLE_TIMING:
        parse_start = timer()

    parse_tree = python_parser3.parse(open('test.py', 'r').read())

    if ENABLE_TIMING:
        parse_end = timer()
        exec_start = timer()

    # Main loop
    for inst in parse_tree.children:
        run_instruction(inst)

    if ENABLE_TIMING:
        exec_end = timer()

    print("Parsing time (seconds): %s" % (parse_end - parse_start,))
    print("Execution time (seconds): %s" % (exec_end - exec_start,))

    global_frame.dump()


main()
