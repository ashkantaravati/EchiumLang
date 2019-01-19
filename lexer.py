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
        # Comma
        self.lexer.add('COMMA', r',')
        # Operators
        self.lexer.add('MUL', r'\*')
        self.lexer.add('EQU', r'=')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # String
        self.lexer.add('STRING', r"""
        \"([^\\\"]|\\.)*\"
        """)
        # Identifier
        self.lexer.add('IDENTIFIER', r"[a-zA-Z_][a-zA-Z0-9_]")
        # Ignore spaces
        self.lexer.ignore(r'\s+')
    def get_rules(self):
        return [rule.name for rule in self.lexer.rules]
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()