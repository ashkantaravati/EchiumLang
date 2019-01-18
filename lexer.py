from rply import LexerGenerator
from utils import get_id_tokens


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # dynamic tokens
        for item in get_id_tokens():
            self.lexer.add(item[0],item[1])
        # braces
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('OPEN_CURLY', r'{')
        self.lexer.add('CLOSE_CURLY', r'}')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('MUL', r'\*')
        self.lexer.add('EQU', r'=')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()