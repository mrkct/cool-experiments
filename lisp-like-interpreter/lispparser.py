from enum import Enum


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            return False

class TokenType(Enum):
    NUMERIC = 0
    STRING = 1
    OPERAND = 2
    PARENTHESIS_OPEN = 3
    PARENTHESIS_CLOSE = 4
    EOF = 5

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __repr__(self):
        return "<{}, {}>".format(self.type, self.value)

class Parser():
    def __init__(self, program):
        self.program = program.strip()
        self.position = 0
    
    def hasNext(self):
        return self.position < len(self.program)

    def next(self):
        if self.position >= len(self.program):
            return Token(TokenType.EOF, "")
        
        in_string = False
        current_token = ""
        while self.position < len(self.program):
            character = self.program[self.position]
            
            if self.is_parenthesis(character) and not in_string:
                if len(current_token) > 0:
                    return self.identifyToken(current_token)
                self.position += 1
                if self.is_open_parenthesis(character):
                    return Token(TokenType.PARENTHESIS_OPEN, character)
                else:
                    return Token(TokenType.PARENTHESIS_CLOSE, character)
            
            if self.is_string_delimiter(character):
                in_string = not in_string
            
            if self.is_separator(character) and not in_string:
                self.position += 1
                if len(current_token) == 0:
                    continue
                current_token += character
                return self.identifyToken(current_token)
            
            if not self.is_whitespace(character) or in_string:
                current_token += character
            self.position += 1
        
        return Token(TokenType.EOF, current_token)

    def identifyToken(self, string_token):
        if len(string_token) == 0:
            return Token(TokenType.EOF, string_token)
        elif string_token[-1] == string_token[0] and self.is_string_delimiter(string_token[0]):
            return Token(TokenType.STRING, string_token[1:-1]) 
        elif is_number(string_token):
            return Token(TokenType.NUMERIC, string_token.strip())
        else:
            return Token(TokenType.OPERAND, string_token.strip())

    def is_string_delimiter(self, character):
        return character in ['"', "'"]

    def is_separator(self, character):
        return character in [' ', '\n', '\t', '"', "'"]
    
    def is_parenthesis(self, character):
        return character in ['(', ')', '[', ']', '{', '}']
    
    def is_open_parenthesis(self, character):
        return character in ['(', '[', '{']
    
    def is_whitespace(self, character):
        return character in [' ', '\n', '\t']