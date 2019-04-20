# Lisp-like Interpreter
## What is this
A parser & interpreter for a lisp-like language. While the parser is pretty much complete, the interpreter still needs a bit of work to implement some of the features to make it usable.

## How to run it
Open `interpreter.py` and write your code in the program variable as a string. Run

    python interpreter.py

## What is missing
- Support for function macros
- More basic operations, stuff like some math operators('-', '/'), some I/O functions and control flow

## Notes
- Because of how the Interpreter.eval function is written, to implement the `def` function the name of the defined variable needs to be in quotes like this `(def 'pi' 3.14)`
- All parenthesis are treated the same way, but you still need to match parenthesis with the same type
- Not all parser & interpreter errors are handled correctly, don't always expect pretty error messages when your program doesn't work