from settings import OUTPUT,TEMPLATE,IDENTIFIERS
import sys
def fetch_string(path):
    f = open(path)
    text = f.read()
    return text

def commit_string(contents,path):
    f = open(path,'w')
    return f.write(contents)

def get_template():
    return fetch_string(TEMPLATE)

def save_output(contents):
    f = commit_string(contents,OUTPUT)
    return f


def build_tag(tag_id, attrs='', contents=''):
    tag = f'''<{tag_id} {attrs}>
    {contents}
    </{tag_id}>
    '''
    return tag

def get_input_code():
    with open(sys.argv[1],'r') as in_file:
        return in_file.read()

def render_in_template(content):
    template = get_template()
    rendered = template.format(content)
    return rendered

def get_id_tokens():
    x = [(y.upper(),y) for y in IDENTIFIERS]
    return x