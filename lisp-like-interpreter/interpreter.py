from lispparser import Parser, TokenType, Token


def Lisp_print(state, arguments):
    for x in arguments[1:]:
        print(x, end="")

def Lisp_add(state, arguments):
    return sum(arguments[1:])

def Lisp_mul(state, arguments):
    print("arguments {}".format(arguments))
    total = 1
    for val in arguments[1:]:
        total *= val
    
    return total

def Lisp_def(state, arguments):
    if len(arguments) < 3:
        raise ArgumentsError("def", "<name>, <value>")
    state[arguments[1]] = arguments[2]

class LispFunction():
    def __init__(self, built_in, content):
        self.built_in = built_in
        self.content = content
    
    def __repr__(self):
        if self.built_in:
            return "<built in, {}>".format(self.content.__name__)
        else:
            return "<macro, {}>".format(self.content)

class TokenError(Exception):
    def __init__(self, token):
        message = "Unknown token '{}'".format(token)
        super(TokenError, self).__init__(message)

class ArgumentsError(Exception):
    def __init__(self, function, expected=""):
        message = "Called function {} with wrong argument count or types"
        if expected != "":
            message += ". Expected {}".format(expected)
        super(ArgumentsError, self).__init__(message)

class Interpreter():
    def __init__(self):
        self.state = dict()
        self.state["+"] = LispFunction(True, Lisp_add)
        self.state["*"] = LispFunction(True, Lisp_mul)
        self.state["print"] = LispFunction(True, Lisp_print)
        self.state["def"] = LispFunction(True, Lisp_def)
    
    def createAST(self, parser):
        ast = []
        while parser.hasNext():
            token = parser.next()
            if token.type == TokenType.PARENTHESIS_OPEN:
                ast.append(self.createAST(parser))
            elif token.type == TokenType.PARENTHESIS_CLOSE:
                return ast
            else:
                ast.append(token)
        
        return ast


    def eval(self, ast):
        if type(ast) is list:
            ast = list(map(lambda t: self.eval(t), ast))
            if type(ast[0]) is LispFunction:
                return ast[0].content(self.state, ast)
            else:
                return ast
        elif type(ast) is Token:
            if ast.type == TokenType.OPERAND:
                if ast.value not in self.state:
                    raise TokenError(ast.value)
                return self.state[ast.value]
            elif ast.type == TokenType.NUMERIC:
                return float(ast.value)
            elif ast.type == TokenType.STRING:
                return ast.value
        else:
            return ast


program = """
(
    (def "pi" 3.14)
    (def "primes" [1 2 3 5 7])
    (print 
        "Il risultato è: " 
        (* 
            5 
            (+ 1 2 3 4 5 ) 
        )
        "\n"
        "PI: "
        pi
        "\n"
    )
)"""

parser = Parser(program)
interpreter = Interpreter()
ast = interpreter.createAST(parser)
interpreter.eval(ast)