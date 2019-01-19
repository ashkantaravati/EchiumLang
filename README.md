# Introduction
Echium is a decalarative script that simplifies the creation of documents with SGML-derived syntax. Echium does not have predifined elements and template.

# Development
## Current Stage
Not working Actually!
Identifiers are currently harcoded in a python dictionary in `settings.py`, which should later be replaced by an external `components.json` file that describes components and their static attributes.

# Usage

## Running Echium
``` python3 echium.py filename.ec ```
## Intended Syntax
```
component[("attrKey"="attrValue","attrKey"="attrValue", ...)] [{
    [component[][][];...|"plain text"]
}] [* 0~255];
```
## Example Code
```
page("color"="black"){
nav{
    link;
    link(href="example.com"){
        image("src"="img.png","data-x"="22")
    };
    empty_link * 5;
    logo("src"="logo.png");
};
paragraph{
    " lorem ipsum dolor sit amet "
}
};

```
`nav`,`link`,`empty_link`,`logo` are identifiers that are externally described in a COMPONENTS dictionary in `settings.py`.
`empty_link` is inherited from `link`.

In this example `page` is an alias for a predefined tag+class hierarchy, described in the components.json file, which after compilation represents a beautifully-designed page template with CSS classes from desired CSS framework

` empty_link * 5; ` means that we need 5 `empty_link` components to be rendered at that point of our document.


# Dependencies
* appdirs==1.4.3
* rply==0.7.6




# Token Regular Expression Rules
```
OPEN_PAREN : \(
CLOSE_PAREN : \)
OPEN_CURLY : {
CLOSE_CURLY : }
SEMI_COLON : \;
COMMA : ,
MUL : \*
EQU : =
NUMBER : \d+
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]
STRING : \"([^\\\"]|\\.)*\"
```

# Grammar Production Specification
```
%token OPEN_PAREN CLOSE_PAREN OPEN_CURLY CLOSE_CURLY
%token SEMI_COLON COMMA
%token MUL EQU
%token NUMBER
%token IDENTIFIER
%token STRING

statement
    : IDENTIFIER parameter_list_specifier block_specifier quantity_specifier SEMI_COLON
    | empty
    ;

parameter_list_specifier
    : OPEN_PAREN parameter_list CLOSE_PAREN
    | empty
    ;

block_specifier
    : OPEN_CURLY statement_list CLOSE_CURLY
    | empty
    ;

statement_list
    : statement
    | statement_list statement
    | plain_text
    ;

parameter_list
	: parameter_declaration
	| parameter_list COMMA parameter_declaration
	;

parameter_declaration
	: STRING EQU STRING
    | empty
    ;

quantity_specifier
    : MUL NUMBER
    | empty
    ;

plain_text
    : STRING
    | empty
    ;

empty
    :
    ;

```

