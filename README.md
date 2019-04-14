# ToyPy

An toy Python 3 interpreter written in pure Python, just for fun.

### Features
- Uses the lark grammar parser - https://github.com/lark-parser/lark
- Supports variable assignment with arithmetic expressions

### Working example
Test file - `test.py`:
```python3
# The parser handles order of operations, making our interpreter more simple
x = 3 + 16 * 2
y = 5 - 16 / 2
z = 5 - 16 / 2 * 52 + 9 * 2 / 18 + 82 - (52 / 2) / 82 - 2

# Test reassignment
b = 5 + 1
b = 6 + 2
```

Execution:
```
# The interpreter reads a file called test.py
> python interpreter.py
Parsing time (seconds): 0.0014879070000000105
Execution time (seconds): 3.261599999992981e-05
========= Stack Locals ==========
{'x': 35, 'y': -3.0, 'z': -330.3170731707317, 'b': 8}
```

### Future Work
- Redesign all data objects to use objects https://docs.python.org/3.7/reference/datamodel.html
- See data type implementations in Python to Go transcompiler for inspiration on core type implementations https://github.com/google/grumpy/tree/master/runtime
- Implement more features such as function calls with their own stack frames
- Refactor the `run_instruction` main loop to support many data handlers
- Implement a `print()` function
- Allow any file name to be run in the interpreter
- Have more fun
