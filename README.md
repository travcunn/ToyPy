# ToyPy

An toy Python 3 interpreter written in pure Python, just for fun.

### Features
- Uses the lark grammar parser - https://github.com/lark-parser/lark
- Supports variable assignment with basic arithmetic expressions

### Working example
Test file - `test.py`:
```python3
# The parser handles order of operations, making our interpreter more simple
x = 3 + 16 * 2
y = 5 - 16 / 2

# Test reassignment
z = 5 + 1
z = 6 + 2
```

Execution:
```
> python parse.py
Parsing time (seconds): 0.0010666940000001457
Execution time (seconds): 1.937300000021125e-05
========= Stack Locals ==========
{'x': 35, 'y': -3.0, 'z': 8}
```

### Future Work
- Redesign all data objects to use objects https://docs.python.org/3.7/reference/datamodel.html
- Implement more features such as function calls with their own stack frames
- Refactor the `run_instruction` main loop to support many data handlers
- Implement a `print()` function
- Have more fun
