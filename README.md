# Goal
Being decoupled from HTML, this language can be used to produce SGML-derived outputs dynamically with a component-based method.

# Example Intended Code
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
`top_nav`,`link`,`empty_link`,`logo` are identifiers that are externally described in a component dictionary. `empty_link` is inherited from `link`.

# Dependencies
* appdirs==1.4.3
* rply==0.7.6

# Usage
``` python3 echium.py filename.ec ```


# Token RegExp Rules
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

# Grammar Specification
```
%token OPEN_PAREN CLOSE_PAREN OPEN_CURLY CLOSE_CURLY
%token SEMI_COLON COMMA
%token MUL EQU
%token NUMBER
%token IDENTIFIER
%token STRING

statement
    : IDENTIFIER parameter_list_specifier block_specifier | quantity_specifier SEMI_COLON
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

