import re
import sys
from utils import save_output,build_tag,get_input_code,render_in_template
from lexer import Lexer
from parser import Parser

code = get_input_code()
print(code)

lexer = Lexer().get_lexer()
tokens = lexer.lex(code)

for token in tokens:
    print(token)
token_names = lexer.get_rules()
pg = Parser(token_names)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

# lexing phase --> tokenize code
# expr_pattern = r'(\w+(\(.*\))?( \* \d+)?;)'
# tag_pattern = r'(\w+)'
# tokens = re.search(expr_pattern, code)

# token = tokens.group(0)
# parsing phase --> build parse tree
# component = re.search(tag_pattern, token).group(0)
# code generation phase --> realize components
# tag_id = COMPONENTS['link']
# alternated = build_tag(tag_id,'')
# ouput
# result = render_in_template(alternated)
# save_output(result)
