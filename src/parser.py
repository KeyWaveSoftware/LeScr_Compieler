# parser.py

from lexer import Lexer, Token

class AST:
    pass

class ReturnNode(AST):
    def __init__(self, value):
        self.value = value

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Syntaxfehler')

    def parse(self):
        nodes = []
        while self.current_token.type != 'EOF':
            if self.current_token.type == 'RETURN':
                self.current_token = self.lexer.get_next_token()  # zum nächsten Token
                if self.current_token.type == 'INTEGER':
                    value = self.current_token.value
                    nodes.append(ReturnNode(value))
                    self.current_token = self.lexer.get_next_token()  # zum nächsten Token
                if self.current_token.type == 'SEMICOLON':
                    self.current_token = self.lexer.get_next_token()  # zum nächsten Token
                else:
                    self.error()
            else:
                self.error()
        return nodes
