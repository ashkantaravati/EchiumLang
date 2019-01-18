# Goal
Being decoupled from HTML, this language can be used to produce SGML-derived outputs dynamically with a component-based method.

# Example Code
```
top_nav{
    link;
    link(href="example.com"){
        image(src="img.png")
    };
    empty_link * 5;
    logo(src="logo.png");
};



```
`top_nav`,`link`,`empty_link`,`logo` are identifiers that are externally described in a component dictionary. `empty_link` is inherited from `link`.

# Dependencies
* appdirs==1.4.3
* rply==0.7.6
# Usage
``` python3 echium.py filename.ec ```


# RegExp (...)
```
expr = (\w+(\(.*\))?( \* \d+)?;)
```

# Grammar Specification
```
%token IDENTIFIER NUMBER STRING_LITERAL

statement
    : ';'
    | IDENTIFIER ';'
    | IDENTIFIER '(' parameter_list ')' ';'
    | IDENTIFIER '{' statement_list '}' ';'
    | IDENTIFIER quantity_specifier ';'
    | IDENTIFIER '(' parameter_list ')' quantity_specifier ';'
    | IDENTIFIER '(' parameter_list ')' '{' statement_list '}' ';'
    | IDENTIFIER '{' statement_list '}' quantity_specifier ';'
    | IDENTIFIER '(' parameter_list ')' '{' statement_list '}' quantity_specifier ';'
    ;
statement_list
    : statement
    | statement_list statement
parameter_list
	: parameter_declaration
	| parameter_list ',' parameter_declaration
	;
parameter_declaration
	: STRING_LITERAL '=' STRING_LITERAL
    ;
quantity_specifier
    : '*' NUMBER

```