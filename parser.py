from rply import ParserGenerator
from ast import Num, MulStr


class Parser():
    def __init__(self, token_names):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            token_names
        )

    def parse(self):
        @self.pg.production('statement : IDENTIFIER parameter_list_specifier block_specifier quantity_specifier SEMI_COLON')
        @self.pg.production('statement : empty')
        def statement(p):
            # logic
            pass
            

        @self.pg.production('parameter_list_specifier : OPEN_PAREN parameter_list CLOSE_PAREN')
        @self.pg.production('parameter_list_specifier : empty')
        def parameter_list_specifier(p):
            # logic
            pass

        @self.pg.production('block_specifier : OPEN_CURLY statement_list CLOSE_CURLY')        
        @self.pg.production('block_specifier : empty')
        def block_specifier(p):
            # logic
            pass
        
        @self.pg.production('statement_list : statement')        
        @self.pg.production('statement_list : statement_list statement')
        @self.pg.production('statement_list : plain_text')
        def statement_list(p):
            # logic
            pass

        @self.pg.production('parameter_list : parameter_declaration')
        @self.pg.production('parameter_list : parameter_list COMMA parameter_declaration')
        def parameter_list(p):
            # logic
            pass
        
        @self.pg.production('parameter_declaration : STRING EQU STRING')
        @self.pg.production('parameter_declaration : empty')
        def parameter_declaration(p):
            # logic
            pass

        @self.pg.production('quantity_specifier : MUL NUMBER')
        @self.pg.production('quantity_specifier : empty')
        def quantity_specifier(p):
            # logic
            pass
    
        @self.pg.production('plain_text : STRING')
        @self.pg.production('plain_text : empty')
        def plain_text(p):
            # logic
            pass


        # success area begins here:
        @self.pg.production('quantity_specifier : MUL NUMBER')
        def quantity_specifier(p):
            return Number(p[0].value)

        @self.pg.production('empty :')
        def empty(p):
            pass

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()